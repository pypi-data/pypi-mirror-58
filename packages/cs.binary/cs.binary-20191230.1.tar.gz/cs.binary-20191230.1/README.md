Facilities associated with binary data parsing and transcription.


*Latest release 20191230.1*:
Docstring updates. Semantic changes were in the previous release.

Facilities associated with binary data parsing and transcription.

Note: this module requires Python 3 and recommends Python 3.6+
because it uses abc.ABC, because a Python 2 bytes object is too
weak (just a `str`) as also is my `cs.py3.bytes` hack class and
because the keyword based `Packet` initiialisation benefits from
keyword argument ordering.

In the description below I use the word "chunk" to mean a piece
of binary data obeying the buffer protocol, almost always a
`bytes` instance or a `memoryview`, but in principle also things
like `bytearray`.

The classes in this module support easy parsing of binary data
structures.

The functions and classes in this module the following:

The two base classes for binary data:
* `PacketField`: an abstract class for a binary field, with a
  factory method to parse it, a transcription method to transcribe
  it back out in binary form and usually a `.value` attribute
  holding the parsed value.
* `Packet`: a `PacketField` subclass for parsing multiple
  `PacketField`s into a larger structure with ordered named
  fields.
  The fields themselves may be `Packet`s for complex structures.


Several presupplied subclasses for common basic types such
as `UInt32BE` (an unsigned 32 bit big endian integer).

Classes built from `struct` format strings:
* `struct_field`: a factory for making PacketField classes for
  `struct` formats with a single value field.
* `multi_struct_field` and `structtuple`: factories for making
  `PacketField`s from `struct` formats with multiple value
  fields;
  `structtuple` makes `PacketField`s which are also `namedtuple`s,
  supporting trivial access to the parsed values.

You don't need to make fields only from binary data; because
`PacketField.__init__` takes a post parse value, you can also
construct `PacketField`s from scratch with their values and
transcribe the resulting binary form.

Each `PacketField` subclass has the following methods:
* `transcribe`: easily return the binary transcription of this field,
  either directly as a chunk (or for convenience, also None or
  an ASCII str) or by yielding successive binary data.
* `from_buffer`: a factory to parse this field from a
  `cs.buffer.CornuCopyBuffer`.
* `from_bytes`: a factory to parse this field from a chunk with
  an optional starting offset; this is a convenience wrapper for
  `from_buffer`.

That may sound a little arcane, but we also supply:
* `flatten`: a recursive function to take the return from any
  `transcribe` method and yield chunks, so copying a packet to
  a file or elsewhere can always be done by iterating over
  `flatten(field.transcribe())` or via the convenience
  `field.transcribe_flat()` method which calls `flatten` itself.
* a `CornuCopyBuffer` is an easy to use wrapper for parsing any
  iterable of chunks, which may come from almost any source.
  It has a bunch of convenient factories including:
  `from_bytes`, make a buffer from a chunk;
  `from_fd`, make a buffer from a file descriptor;
  `from_file`, make a buffer from a file-like object;
  `from_mmap`, make a buffer from a file descriptor using a
  memory map (the `mmap` module) of the file, so that chunks
  can use the file itself as backing store instead of allocating
  and copying memory.
  See the `cs.buffer` module for further detail.

When parsing a complex structure
one must choose between subclassing `PacketField` or `Packet`.
An effective guideline is the degree of substructure.

A `Packet` is designed for deeper structures;
all of its attributes are themselves `PacketField`s
(or `Packet`s, which are `PacketField` subclasses).
The leaves of this hierarchy will be `PacketField`s,
whose attributes are ordinary types.

By contrast, a `PacketField`'s attributes are "flat" values:
the plain post-parse value, such as a `str` or an `int`
or some other conventional Python type.

The base case for `PacketField`
is a single such value, named `.value`,
and the natural implementation
is to provide a `.value_from_buffer` method
which returns the basic single value
and the corresponding `.transcribe_value` method
to return or yield its binary form
(directly or in pieces respectively).

However,
you can handle multiple attributes with this class
by instead implementing:
* `__init__`: to compose an instance from post-parse values
  (and thus from scratch rather than parsed from existing binary data)
* `from_buffer`: class method to parse the values
  from a `CornuCopyBuffer` and call the class constructor
* `transcribe`: to return or yield the binary form of the attributes

Cameron Simpson <cs@cskk.id.au> 22jul2018

## Class `BSData`

MRO: `PacketField`, `abc.ABC`  
A run length encoded data chunk, with the length encoded as a BSUInt.

## Class `BSSFloat`

MRO: `PacketField`, `abc.ABC`  
A float transcribed as a BSString of str(float).

## Class `BSString`

MRO: `PacketField`, `abc.ABC`  
A run length encoded string, with the length encoded as a BSUInt.

## Class `BSUInt`

MRO: `PacketField`, `abc.ABC`  
A binary serialsed unsigned int.

This uses a big endian byte encoding where continuation octets
have their high bit set. The bits contributing to the value
are in the low order 7 bits.

## Class `BytesesField`

MRO: `PacketField`, `abc.ABC`  
A field containing a list of bytes chunks.

The following attributes are defined:
* `value`: the gathered data as a list of bytes instances,
  or None if the field was gathered with `discard_data` true.
* `offset`: the starting offset of the data.
* `end_offset`: the ending offset of the data.

The `offset` and `end_offset` values are recorded during the
parse, and may become irrelevant if the field's contents are
changed.

## Class `BytesField`

MRO: `PacketField`, `abc.ABC`  
A field of bytes.

## Class `BytesRunField`

MRO: `PacketField`, `abc.ABC`  
A field containing a continuous run of a single bytes value.

The following attributes are defined:
* `length`: the length of the run
* `bytes_value`: the repeated bytes value

The property `value` is computed on the fly on every reference
and returns a value obeying the buffer protocol: a bytes or
memoryview object.

## Class `EmptyPacketField`

MRO: `PacketField`, `abc.ABC`  
An empty data field, used as a placeholder for optional
fields when they are not present.

The singleton `EmptyField` is a predefined instance.

## Function `fixed_bytes_field(length, class_name=None)`

Factory for `BytesField` subclasses built from fixed length byte strings.

## Function `flatten(chunks)`

Flatten `chunks` into an iterable of `bytes` instances.

This exists to allow subclass methods to easily return ASCII
strings or bytes or iterables or even `None`, in turn allowing
them simply to return their superclass' chunks iterators
directly instead of having to unpack them.

## Class `Float64BE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'>d'`.

## Class `Float64LE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'<d'`.

## Class `Int16BE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'>h'`.

## Class `Int16LE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'<h'`.

## Class `Int32BE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'>l'`.

## Class `Int32LE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'<l'`.

## Class `ListField`

MRO: `PacketField`, `abc.ABC`  
A field which is a list of other fields.

## Function `multi_struct_field(struct_format, subvalue_names=None, class_name=None)`

Factory for `PacketField` subclasses build around complex struct formats.

Parameters:
* `struct_format`: the struct format string
* `subvalue_names`: an optional namedtuple field name list;
  if supplied then the field value will be a namedtuple with
  these names
* `class_name`: option name for the generated class

## Class `Packet`

MRO: `PacketField`, `abc.ABC`  
Base class for compound objects derived from binary data.

### Method `Packet.__init__(self, **fields)`

Initialise the `Packet`.

A `Packet` is its own `.value`.

If any keyword arguments are provided, they are used as a
mapping of `field_name` to `Field` instance, supporting
direct construction of simple `Packet`s.
From Python 3.6 onwards keyword arguments preserve the calling order;
in Python versions earlier than this the caller should
adjust the `Packet.field_names` list to the correct order after
initialisation.

## Class `PacketField`

MRO: `abc.ABC`  
A record for an individual packet field.

This normally holds a single value, such as a int of a particular size
or a string.

There are 2 basic ways to implement a `PacketField` subclass.

For the simple case subclasses should implement two methods:
* `value_from_buffer`:
  parse the value from a `CornuCopyBuffer` and returns the parsed value
* `transcribe_value`:
  transcribe the value as bytes

Sometimes a `PacketField` may be slightly more complex
while still not warranting (or perhaps fitting)
the formality of a `Packet` with its multifield structure.

One example is the `cs.iso14496.UTF8or16Field` class.
This supports an ISO14496 UTF8 or UTF16 string field,
as as such has 2 attributes:
* `value`: the string itself
* `bom`: a UTF16 byte order marker or `None`;
  `None` indicates that the string should be encoded as UTF-8
  and otherwise the BOM indicates UTF16 big endian or little endian.

To make this subclass it defines these methods:
* `from_buffer`:
  to read the optional BOM and then the following encoded string;
  it then returns the new `UTF8or16Field`
  initialised from these values via `cls(text, bom=bom)`.
* `transcribe`:
  to transcribe the option BOM and suitably encoded string.
The instance method `transcribe` is required because the transcription
requires knowledge of the BOM, an attribute of an instance.

### Method `PacketField.__init__(self, value=None)`

Initialise the `PacketField`.
If omitted the inial field `value` will be `None`.

## Function `struct_field(struct_format, class_name)`

Factory for `PacketField` subclasses built around a single struct format.

Parameters:
* `struct_format`: the struct format string, specifying a
  single struct field
* `class_name`: the class name for the generated class

Example:

    >>> UInt16BE = struct_field('>H', class_name='UInt16BE')
    >>> UInt16BE.__name__
    'UInt16BE'
    >>> UInt16BE.format
    '>H'
    >>> UInt16BE.struct   #doctest: +ELLIPSIS
    <Struct object at ...>
    >>> field, offset = UInt16BE.from_bytes(bytes((2,3,4)))
    >>> field
    UInt16BE(515)
    >>> offset
    2
    >>> field.value
    515

## Function `structtuple(class_name, struct_format, subvalue_names)`

Convenience wrapper for multi_struct_field.

## Class `UInt16BE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'>H'`.

## Class `UInt16LE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'<H'`.

## Class `UInt32BE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'>L'`.

## Class `UInt32LE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'<L'`.

## Class `UInt64BE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'>Q'`.

## Class `UInt64LE`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'<Q'`.

## Class `UInt8`

MRO: `PacketField`, `abc.ABC`  
A `PacketField` which parses and transcribes the struct format `'B'`.

## Class `UTF16NULField`

MRO: `PacketField`, `abc.ABC`  
A NUL terminated UTF-16 string.

### Method `UTF16NULField.__init__(self, value, *, encoding)`

Initialise the `PacketField`.
If omitted the inial field `value` will be `None`.

## Class `UTF8NULField`

MRO: `PacketField`, `abc.ABC`  
A NUL terminated UTF-8 string.

## Function `warning(msg, *a, f=None)`

Issue a formatted warning message.



# Release Log

*Release 20191230.1*:
Docstring updates. Semantic changes were in the previous release.

*Release 20191230*:
ListField: new __iter__ method.
Packet: __str__: accept optional `skip_fields` parameter to omit some field names.
Packet: new .add_from_value method to add a named field with a presupplied value.
Packet: new remove_field(field_name) and pop_field() methods to remove fields.
BytesesField: __iter__ yields the bytes values, transcribe=__iter__.
PacketField: propagate keyword arguments through various methods, required for parameterised PacketFields.
New UTF16NULField, a NUL terminated UTF16 string.
PacketField: provide a default `.transcribe_value` method which makes a new instance and calls its `.transcribe` method.
Documentation update and several minor changes.

*Release 20190220*:
Packet.self_check: fields without a sanity check cause a warning, not a ValueError.
New Float64BE, Float64LE and BSSFloat classes for IEEE floats and floats-as-strings.
Additional module docstringage on subclassing Packet and PacketField.
BSString: drop redundant from_buffer class method.
PacketField.__init__: default to value=None if omitted.

*Release 20181231*:
flatten: do not yield zero length bytelike objects, can be misread as EOF on some streams.

*Release 20181108*:
New PacketField.transcribe_value_flat convenience method to return a flat iterable of bytes-like objects.
New PacketField.parse_buffer generator method to parse instances of the PacketField from a buffer until end of input.
New PacketField.parse_buffer_values generator method to parse instances of the PacketField from a buffer and yield the `.value` attribute until end of input.

*Release 20180823*:
Some bugfixes.
Define PacketField.__eq__.
BSUInt, BSData and BSString classes implementing the serialisations from cs.serialise.
New PacketField.value_from_bytes class method.
New PacketField.value_from_buffer method.

*Release 20180810.2*:
Documentation improvements.

*Release 20180810.1*:
Improve module description.

*Release 20180810*:
BytesesField.from_buffer: make use of the buffer's skipto method if discard_data is true.

*Release 20180805*:
Packet: now an abstract class, new self_check method initially checking the
PACKET_FIELDS class attribute against the instance, new methods get_field
and set_field to fetch or replace existing fields, allow keyword arguments
to initialise the Packet fields and document the dependency on keyword
argument ordering.
PacketField: __len__ computed directory from a transcribe, drop other __len__
methods.
EmptyField singleton to use as a placeholder for missing optional fields.
BytesField: implement value_s and from_buffer.
multi_struct_field: implement __len__ for generated class.
flatten: treat memoryviews like bytes.
Assorted docstrings and fixes.

*Release 20180801*:
Initial PyPI release.
