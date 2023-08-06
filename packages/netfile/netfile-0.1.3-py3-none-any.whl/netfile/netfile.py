#!/usr/bin/python3

from collections import namedtuple
import dataclasses
import enum
import io
import logging
import os
import struct

import pefile

### IOStream Reader Helpers ###

def read_padded_string(f, alignment=4):
    name = b''
    while True:
        data = f.read(alignment)
        name = name + data
        if data[-1] == 0x00:
            break
    fzero = name.find(0)
    return name[:fzero].decode()


def read_null_string(f):
    strdata = b''
    while True:
        data = f.read(1)
        strdata = strdata + data
        if data[0] == 0x00:
            break
    return strdata[:-1].decode()


def read_encoded_int(f):
    data = f.read(1)
    if not (data[0] & 0x80):
        return data[0]
    data = data + f.read(1)
    if (data[0] & 0xC0) == 0x80:
        data = bytes([(data[0] & 0x3F), data[1]])
        # Yes, the bit order is effectively Big Endian here...
        return struct.unpack('>H', data)[0]
    data = data + f.read(2)
    assert((data[0] & 0xE0) == 0xC0)
    data = bytes([(data[0] & 0x1F)]) + data[1:4]
    return struct.unpack('>I', data)[0]


def read_uint(f, size):
    if size == 1:
        fmt = '<B'
    elif size == 2:
        fmt = '<H'
    elif size == 4:
        fmt = '<I'
    elif size == 8:
        fmt = '<Q'
    else:
        raise Exception('Unimplemented integer read size')
    return struct.unpack(fmt, f.read(size))[0]


def read_blob(f):
    n = read_encoded_int(f)
    data = f.read(n)
    return data


def read_unicode_string(f):
    data = read_blob(f)
    return data[:-1].decode('UTF-16-le')


### Classes ###

Segment = namedtuple('Segment', ['offset', 'size'])

@dataclasses.dataclass
class PtrConfig:
    str: int
    guid: int
    blob: int
    TypeDefOrRef: int = -1
    HasConstant: int = -1
    HasCustomAttribute: int = -1
    HasFieldMarshal: int = -1
    HasDeclSecurity: int = -1
    MemberRefParent: int = -1
    HasSemantics: int = -1
    MethodDefOrRef: int = -1
    MemberForwarded: int = -1
    Implementation: int = -1
    CustomAttributeType: int = -1
    ResolutionScope: int = -1
    TypeOrMethodDef: int = -1

class Table(enum.Enum):
    UNKNOWN = -2
    UNUSED = -1
    Module = 0
    TypeRef = 1
    TypeDef = 2
    Field = 4
    MethodDef = 6
    Param = 8
    InterfaceImpl = 9
    MemberRef = 10
    Constant = 11
    CustomAttribute = 12
    FieldMarshal = 13
    DeclSecurity = 14
    ClassLayout = 15
    FieldLayout = 16
    StandAloneSig = 17
    EventMap = 18
    Event = 20
    PropertyMap = 21
    Property = 23
    MethodSemantics = 24
    MethodImpl = 25
    ModuleRef = 26
    TypeSpec = 27
    ImplMap = 28
    FieldRVA = 29
    Assembly = 32
    AssemblyProcessor = 33
    AssemblyOS = 34
    AssemblyRef = 35
    AssemblyRefProcessor = 36
    AssemblyRefOS = 37
    File = 38
    ExportedType = 39
    ManifestResource = 40
    NestedClass = 41
    GenericParam = 42
    MethodSpec = 43
    GenericParamConstraint = 44

    def row_size(self, ptrsizes, idxcfg):
        tab = {
            Table.Module: 2 + ptrsizes.str + (3 * ptrsizes.guid),
            Table.TypeRef: ptrsizes.ResolutionScope + (2 * ptrsizes.str),
            Table.TypeDef: 4 + (2 * ptrsizes.str) + ptrsizes.TypeDefOrRef + idxcfg.Field + idxcfg.MethodDef,
            Table.Field: 2 + ptrsizes.str + ptrsizes.blob,
            Table.MethodDef: 8 + ptrsizes.str + ptrsizes.blob + idxcfg.Param,
            Table.Param: 4 + ptrsizes.str,
            Table.InterfaceImpl: idxcfg.TypeDef + ptrsizes.TypeDefOrRef,
            Table.MemberRef: ptrsizes.MemberRefParent + ptrsizes.str + ptrsizes.blob,
            Table.Constant: 2 + ptrsizes.HasConstant + ptrsizes.blob,
            Table.CustomAttribute: ptrsizes.HasCustomAttribute + ptrsizes.CustomAttributeType + ptrsizes.blob,
            Table.FieldMarshal: ptrsizes.HasFieldMarshal + ptrsizes.blob,
            Table.DeclSecurity: 2 + ptrsizes.HasDeclSecurity + ptrsizes.blob,
            Table.ClassLayout: 6 + idxcfg.TypeDef,
            Table.FieldLayout: 4 + idxcfg.Field,
            Table.StandAloneSig: ptrsizes.blob,
            Table.EventMap: idxcfg.TypeDef + idxcfg.Event,
            Table.Event: 2 + ptrsizes.str + ptrsizes.TypeDefOrRef,
            Table.PropertyMap: idxcfg.TypeDef + idxcfg.Property,
            Table.Property: 2 + ptrsizes.str + ptrsizes.blob,
            Table.MethodSemantics: 2 + idxcfg.MethodDef + ptrsizes.HasSemantics,
            Table.MethodImpl: idxcfg.TypeDef + (2 * ptrsizes.MethodDefOrRef),
            Table.ModuleRef: ptrsizes.str,
            Table.TypeSpec: ptrsizes.blob,
            Table.ImplMap: 2 + ptrsizes.MemberForwarded + ptrsizes.str + idxcfg.ModuleRef,
            Table.FieldRVA: 4 + idxcfg.Field,
            Table.Assembly: 4 + 8 + 4 + ptrsizes.blob + (2 * ptrsizes.str),
            Table.AssemblyProcessor: 4,
            Table.AssemblyOS: 12,
            Table.AssemblyRef: 8 + 4 + ptrsizes.blob + (2 * ptrsizes.str) + ptrsizes.blob,
            Table.AssemblyRefProcessor: 4 + idxcfg.AssemblyRef,
            Table.AssemblyRefOS: 12,
            Table.File: 4 + ptrsizes.str + ptrsizes.blob,
            Table.ExportedType: 4 + 4 + (2 * ptrsizes.str) + ptrsizes.Implementation,
            Table.ManifestResource: 4 + 4 + ptrsizes.str + ptrsizes.Implementation,
            Table.NestedClass: (2 * idxcfg.TypeDef),
            Table.GenericParam: 2 + 2 + ptrsizes.TypeOrMethodDef + ptrsizes.str,
            Table.MethodSpec: ptrsizes.MethodDefOrRef + ptrsizes.blob,
            Table.GenericParamConstraint: idxcfg.GenericParam + ptrsizes.TypeDefOrRef,
        }
        return tab[self]

IdxConfig = dataclasses.make_dataclass('IdxConfig',
                                       [(tab.name, int,
                                         dataclasses.field(default=2))
                                        for tab in Table])

class ElementType(enum.Enum):
    END = 0x00
    VOID = 0x01
    BOOLEAN = 0x02
    CHAR = 0x03
    I1 = 0x04
    U1 = 0x05
    I2 = 0x06
    U2 = 0x07
    I4 = 0x08
    U4 = 0x09
    I8 = 0x0a
    U8 = 0x0b
    R4 = 0x0c
    R8 = 0x0d
    STRING = 0x0e
    PTR = 0x0f
    BYREF = 0x10
    VALUETYPE = 0x11
    CLASS = 0x12
    VAR = 0x13
    ARRAY = 0x14
    GENERICINST = 0x15
    TYPEDBYREF = 0x16
    I = 0x18
    U = 0x19
    FNPTR = 0x1b
    OBJECT = 0x1c
    SZARRAY = 0x1d
    MVAR = 0x1e
    CMOD_REQD = 0x1f
    CMOD_OPT = 0x20
    INTERNAL = 0x21
    MODIFIER = 0x40
    SENTINEL = 0x41
    PINNED = 0x45
    SYSTYPE = 0x50
    CUSTOMBOXED = 0x51
    RESERVED = 0x52
    CUSTOMFIELD = 0x53


### Table Row Classes ###


class Field:
    """Class representing a row in the Field table"""
    def __init__(self, raw, ptrsizes):
        data = io.BytesIO(raw)
        self.flags = read_uint(data, 2)
        self.name = read_uint(data, ptrsizes.str)
        self.signature = read_uint(data, ptrsizes.blob)
        self.rva = None
        self.parent = None
        self.sig = None
    def parse(self, netb):
        self.sig = FieldSignature(netb.blobs[self.signature])

class TypeDef:
    """Class representing a row in the TypeDef table"""
    def __init__(self, raw, ptrsizes, idxcfg):
        rowsize = Table.TypeDef.row_size(ptrsizes, idxcfg)
        if len(raw) != rowsize:
            raise Exception("Expecting %d bytes got %d" % (rowsize, len(raw)))
        f = io.BytesIO(raw)
        self.flags = read_uint(f, 4)
        self.name = read_uint(f, ptrsizes.str)
        self.namespace = read_uint(f, ptrsizes.str)
        self.extends = read_uint(f, ptrsizes.TypeDefOrRef)
        self.field_list = read_uint(f, idxcfg.Field)
        self.method_list = read_uint(f, idxcfg.MethodDef)
        self.field_list_end = None
        self.method_list_end = None
        self.layout = None
        self.fullname = None


class FieldRVA:
    """Class representing a row in the FieldRVA table"""
    def __init__(self, raw, idxcfg):
        data = io.BytesIO(raw)
        self.rva = read_uint(data, 4)
        self.field = read_uint(data, idxcfg.Field)


class ClassLayout:
    """Class representing a row in the ClassLayout table"""
    def __init__(self, raw, idxcfg):
        data = io.BytesIO(raw)
        self.packing_size = read_uint(data, 2)
        self.class_size = read_uint(data, 4)
        self.parent = read_uint(data, idxcfg.TypeDef)


### Misc Metadata Parsing Classes ###


class TypeDefOrRefOrSpec:
    def __init__(self, n):
        tval = n & 0x3
        if tval == 0x00:
            table = Table.TypeDef
        elif tval == 0x01:
            table = Table.TypeRef
        elif tval == 0x02:
            table = Table.TypeSpec
        self.tval = tval
        self.table = table
        self.value = n >> 2


class TypeInfo:
    """Class representing a Type structure as defined in 11.23.2.12 Type"""
    unsupported = {ElementType.ARRAY, ElementType.CLASS, ElementType.FNPTR,
                   ElementType.GENERICINST, ElementType.MVAR, ElementType.PTR,
                   ElementType.VAR}
    supported = {ElementType.BOOLEAN, ElementType.CHAR, ElementType.I1,
                 ElementType.U1, ElementType.I2, ElementType.U2,
                 ElementType.I4, ElementType.U4, ElementType.I8,
                 ElementType.U8, ElementType.R4, ElementType.R8,
                 ElementType.I, ElementType.U, ElementType.OBJECT,
                 ElementType.STRING, ElementType.VALUETYPE,
                 ElementType.CLASS, ElementType.SZARRAY}
    def __init__(self, f):
        self.elemtype = ElementType(struct.unpack('<B', f.read(1))[0])
        if self.elemtype not in (TypeInfo.supported | TypeInfo.unsupported):
            raise Exception("Unexpected ElementType %s" % self.elemtype.name)
        elif self.elemtype in TypeInfo.unsupported:
            raise Exception("ElementType %s signature parsing unimplemented" % self.elemtype.name)

        if self.elemtype in {ElementType.VALUETYPE, ElementType.CLASS}:
            self.data = TypeDefOrRefOrSpec(read_encoded_int(f))
        if self.elemtype == ElementType.SZARRAY:
            # FIXME: Add CustomMod structure support.
            self.data = TypeInfo(f)
        else:
            # generic type with no parameters; ElemType is sufficient
            pass


class FieldSignature:
    def __init__(self, raw):
        data = io.BytesIO(raw)
        assert(struct.unpack('<B', data.read(1))[0] == 0x06)
        # FIXME: Add CustomMod structure support. TypeInfo will reject these.
        self.type = TypeInfo(data)


### MacDaddy ###


class NETFile:
    def __init__(self, fname):
        # Offsets:
        # Offset of binary assembly data
        self.offset_bin = None
        # Offset,Size of CLI Metadata Root
        self.metadata_root = Segment(None, None)

        # Cached Headers:
        # CLI Metadata Stream Headers
        self.streams = {}

        # Index Size Config Data:
        self.ptrsizes = None

        # Heap data:
        self.strings = {}
        self.ustrings = {}
        self.guids = {}
        self.blobs = {}

        # Raw Table Data:
        self.tables = {}

        # Parsed Table Data:
        self.typedefs = []
        self.fields = []

        # Initialize:
        self.f = open(fname, 'br')
        self.pefile = pefile.PE(fname)

    def relative_to_absolute(self, offset):
        return self.pefile.get_physical_by_rva(offset)

    def _parse_CLI_header(self):
        # See II.25.3.3
        #
        # RVA 15 tells us where the CLR headers start (e.g. 0x2008)
        # Modify the pointer to find the real offset (e.g. 0x208)
        cli_header = self.relative_to_absolute(self.pefile.OPTIONAL_HEADER.DATA_DIRECTORY[14].VirtualAddress)
        logging.debug("CLI header at file offset 0x%x", cli_header)
        self.f.seek(cli_header, os.SEEK_SET)
        cli_size = read_uint(self.f, 4)
        self.offset_bin = cli_header + cli_size
        self.f.seek(4, os.SEEK_CUR)
        self.metadata_root = Segment(*struct.unpack('<II', self.f.read(8)))

    def _parse_metadata_root(self):
        # See II.24.2.1
        abs_offset = self.relative_to_absolute(self.metadata_root.offset)
        self.f.seek(abs_offset, os.SEEK_SET)
        assert(self.f.read(4) == b'BSJB')
        self.f.seek(8, os.SEEK_CUR)
        strlen = read_uint(self.f, 4)
        self.f.seek(strlen + 2, os.SEEK_CUR)
        nstreams = read_uint(self.f, 2)
        logging.debug("%d metadata streams found", nstreams)

        streams = {}
        for _ in range(nstreams):
            offset, length = struct.unpack('<II', self.f.read(8))
            name = read_padded_string(self.f)
            streams[name] = {'offset': offset, 'length': length, 'name': name}
            logging.debug("Stream '%s', offset: 0x%x; raw offset: 0x%x", name, offset, abs_offset + offset)
        self.streams = streams

    def _parse_stream(self, stream_id, readerfn):
        heap_map = {}
        if stream_id not in self.streams:
            return heap_map
        stream = self.streams[stream_id]
        addr = self.relative_to_absolute(self.metadata_root.offset) + stream['offset']
        self.f.seek(addr, os.SEEK_SET)
        while True:
            offset = self.f.tell() - addr
            if offset >= stream['length']:
                break
            heap_map[offset] = readerfn(self.f)
        logging.debug("Found {:d} entries in {:s}".format(len(heap_map), stream['name']))
        return heap_map

    def get_string(self, index):
        try:
            return self.strings[index]
        except KeyError:
            # Some strings are indexed as substrings, fetch them manually:
            stream = self.streams['#Strings']
            addr = self.relative_to_absolute(self.metadata_root.offset) + stream['offset']
            pos = self.f.tell()
            self.f.seek(addr, os.SEEK_SET)
            strdata = read_null_string(self.f)
            self.f.seek(pos, os.SEEK_SET)

            # Cache result:
            self.strings[index] = strdata
            return strdata

    def _parse_strings(self):
        self.strings = self._parse_stream('#Strings', read_null_string)

    def _parse_ustrings(self):
        self.ustrings = self._parse_stream('#US', read_unicode_string)

    def _parse_guids(self):
        self.guids = self._parse_stream('#GUID', lambda f: f.read(16))

    def _parse_blobs(self):
        self.blobs = self._parse_stream('#Blob', read_blob)

    def _parse_streams(self):
        self._parse_strings()
        self._parse_ustrings()
        self._parse_guids()
        self._parse_blobs()

    @staticmethod
    def _table_row_count(tables, table):
        if table in tables:
            return tables[table]['nrows']
        return 0

    @staticmethod
    def _table_row_counts(tables, entries):
        return [NETFile._table_row_count(tables, entry) for entry in entries]

    def _parse_metadata_stream(self):
        addr = self.relative_to_absolute(self.metadata_root.offset) + self.streams['#~']['offset']
        self.f.seek(addr + 6, os.SEEK_SET)
        ptr_config = self.f.read(1)[0]
        ptrsizefn = lambda mask: 4 if (ptr_config & mask) else 2
        self.ptrsizes = PtrConfig(ptrsizefn(0x01), ptrsizefn(0x02), ptrsizefn(0x04))
        self.f.seek(1, os.SEEK_CUR)

        # Which tables do we have?
        tablebits = read_uint(self.f, 8)
        tables = {}
        bitstr = bin(tablebits)[2:]
        for idx, bit in enumerate(reversed(bitstr)):
            if bit == '1':
                tables[Table(idx)] = {}
        logging.debug("Found %d tables", len(tables))

        # Which tables are sorted?
        sortedbits = read_uint(self.f, 8)
        bitstr = bin(sortedbits)[2:]
        for idx, bit in enumerate(reversed(bitstr)):
            try:
                tab = Table(idx)
                if tab in tables:
                    tables[tab]['sorted'] = True if bit == '1' else False
            except ValueError:
                pass

        # Read in table row counts
        for table in tables:
            nrows = read_uint(self.f, 4)
            idxsize = 2 if (nrows < 0x10000) else 4
            tables[table]['nrows'] = nrows
            tables[table]['idxsize'] = idxsize
            logging.debug("Found %s table with %d rows index size %d", table.name, nrows, idxsize)

        # Compute the size of variable-length indices
        def _compute_field_width(tabs):
            maxsize = max(self._table_row_counts(tables, tabs))
            return 4 if maxsize > 2**(16 - int.bit_length(len(tabs) - 1)) else 2

        idxs = {
            'TypeDefOrRef': [
                Table.TypeDef, Table.TypeRef, Table.TypeSpec
            ],
            'HasConstant': [
                Table.Field, Table.Param, Table.Property
            ],
            'HasCustomAttribute': [
                Table.MethodDef, Table.Field, Table.TypeRef, Table.TypeDef,
                Table.Param, Table.InterfaceImpl, Table.MemberRef, Table.Module,
                Table.UNKNOWN, Table.Property, Table.Event,
                # FIXME: What is Table.Permission supposed to be ...?
                Table.StandAloneSig, Table.ModuleRef, Table.TypeSpec,
                Table.Assembly, Table.AssemblyRef, Table.File,
                Table.ExportedType, Table.ManifestResource, Table.GenericParam,
                Table.GenericParamConstraint, Table.MethodSpec
            ],
            'HasFieldMarshal': [
                Table.Field, Table.Param
            ],
            'HasDeclSecurity': [
                Table.TypeDef, Table.MethodDef, Table.Assembly
            ],
            'MemberRefParent': [
                Table.TypeDef, Table.TypeRef, Table.ModuleRef, Table.MethodDef, Table.TypeSpec
            ],
            'HasSemantics': [
                Table.Event, Table.Property
            ],
            'MethodDefOrRef': [
                Table.MethodDef, Table.MemberRef
            ],
            'MemberForwarded': [
                Table.Field, Table.MethodDef
            ],
            'Implementation': [
                Table.File, Table.AssemblyRef, Table.ExportedType
            ],
            'CustomAttributeType': [
                Table.UNUSED, Table.UNUSED, Table.MethodDef, Table.MemberRef, Table.UNUSED
            ],
            'ResolutionScope': [
                Table.Module, Table.ModuleRef, Table.AssemblyRef, Table.TypeRef
            ],
            'TypeOrMethodDef': [
                Table.TypeDef, Table.MethodDef
            ]
        }

        for key, tabs in idxs.items():
            setattr(self.ptrsizes, key, _compute_field_width(tabs))
        logging.debug("%s", str(self.ptrsizes))

        self.idxconfig = IdxConfig()
        for table in tables:
            nrows = tables[table]['nrows']
            # Note; table indices are 1-indexed, so size=1 implies index 1 is valid.
            # size=0xFFFF implies index 0xFFFF is valid.
            idxsize = 4 if nrows > 0xFFFF else 2
            setattr(self.idxconfig, table.name, idxsize)
        logging.debug("%s", str(self.idxconfig))

        # Read in tables
        for table in tables:
            nrows = tables[table]['nrows']
            rowsize = table.row_size(self.ptrsizes, self.idxconfig)
            logging.debug("Reading table %s rows %d, %d bytes each, %d bytes total", table.name, nrows, rowsize, nrows * rowsize)
            rows = []
            for _ in range(nrows):
                rows.append(self.f.read(rowsize))
            tables[table]['rows'] = rows

        # ~ fin ~
        self.tables = tables

    def _parse_table_typedef(self):
        """Convert the raw table into something smarter"""
        if Table.TypeDef not in self.tables:
            return
        typedefs = []
        for typedef in self.tables[Table.TypeDef]['rows']:
            typeobj = TypeDef(typedef, self.ptrsizes, self.idxconfig)
            name = self.get_string(typeobj.name)
            namespace = self.get_string(typeobj.namespace)
            typeobj.fullname = "{}.{}".format(namespace, name)
            if typedefs:
                typedefs[-1].field_list_end = typeobj.field_list
                typedefs[-1].method_list_end = typeobj.method_list
            typedefs.append(typeobj)

        # Last item in list has a default terminus
        if typedefs:
            typedefs[-1].field_list_end = len(self.tables[Table.Field]['rows']) + 1
            typedefs[-1].method_list_end = len(self.tables[Table.MethodDef]['rows']) + 1

        # Correlate to field entries
        for typedef in typedefs:
            fields = []
            for n in range(typedef.field_list, typedef.field_list_end):
                field = self.fields[n - 1]
                field.parent = typedef
                fields.append(field)
            typedef.fields = fields

        # Save results
        self.typedefs = typedefs

    def _parse_table_classlayout(self):
        if Table.ClassLayout not in self.tables:
            return
        for row in self.tables[Table.ClassLayout]['rows']:
            layobj = ClassLayout(row, self.idxconfig)
            self.typedefs[layobj.parent - 1].layout = layobj

    def _parse_table_field(self):
        """Note, this is a lightweight parse that omits signature parsing..."""
        # Because it's hard and complicated!
        if Table.Field not in self.tables:
            return
        fields = []
        for field in self.tables[Table.Field]['rows']:
            fieldobj = Field(field, self.ptrsizes)
            fields.append(fieldobj)
        self.fields = fields

    def _parse_table_fieldrva(self):
        if Table.FieldRVA not in self.tables:
            return
        for rowdata in self.tables[Table.FieldRVA]['rows']:
            rvaobj = FieldRVA(rowdata, self.idxconfig)
            self.fields[rvaobj.field - 1].rva = rvaobj

    def parse(self):
        self._parse_CLI_header()
        self._parse_metadata_root()
        self._parse_streams()
        self._parse_metadata_stream()
        self._parse_table_field()
        self._parse_table_fieldrva()
        self._parse_table_typedef()
        self._parse_table_classlayout()

if __name__ == '__main__':
    import sys
    logging.basicConfig(level=logging.DEBUG)
    binfile = NETFile(sys.argv[1])
    binfile.parse()
