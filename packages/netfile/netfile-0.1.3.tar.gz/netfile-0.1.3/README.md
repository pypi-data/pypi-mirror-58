# Hello World!

netfile is a small .NET executable binary parser. It is capable of reading in
a .NET executable binary (like a .dll) and parsing the metadata structures
in-memory to make programmatic access to this information possible.

# Why?

I wanted to automate the extraction of resources from "compiled" .NET assets,
and doing it from first principles was a learning exercise.

# Notable (Known) Bugs:

* Signature parsing is very rudimentary and incomplete,
  so it is not done by default; you can call the stub using
  Field.parse().

# Notable Missing Features:

* Only the TypeDef, Field, ClassLayout and FieldRVA tables are interpreted
  into right objects right now. The remaining tables are loaded simply as
  collections of raw bytes.

# Do you intend to support this?

Not really. If you find it useful and fix minor issues, I'll happily take
pull requests. If you want to do a major refactor of my hasty first draft,
I'd recommend simply forking the project instead.
