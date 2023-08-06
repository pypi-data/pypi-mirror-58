# Faster STEP-file lexer and parser
# Created: 04.01.2020
# Copyright (c) 2020 Manfred Moitzi
# License: MIT License
from typing import Iterable, Union, Tuple, List, Dict, Optional, TextIO
from string import ascii_letters, digits, ascii_uppercase, hexdigits
from datetime import datetime
from collections import OrderedDict, ChainMap
from io import StringIO
import re

__all__ = [
    'timestamp', 'is_string', 'is_integer', 'is_real', 'is_binary', 'is_reference', 'is_keyword', 'is_enum',
    'is_unset_parameter', 'is_typed_parameter', 'is_parameter_list', 'is_entity', 'is_simple_entity_instance',
    'is_complex_entity_instance', 'keyword', 'reference', 'enum', 'binary', 'unset_parameter',
    'parameter_list', 'simple_entity_instance', 'simple_instance', 'complex_entity_instance', 'new_step_file',
    'load', 'loads', 'readfile', 'STEP_FILE_ENCODING', 'ParseError', 'StepFileStructureError',
]

STEP_FILE_ENCODING = 'iso-8859-1'
END_OF_INSTANCE = ';\n'

EOF = '\a'
BACKSLASH = '\\'
APOSTROPHE = "'"
SPECIAL = '!"*$%&.#+,-()?/:;<=>@[]{|}^`~'
SINGLE_CHAR_TOKENS = ';,*$()='
FIRST_KEYWORD_CHAR = ascii_uppercase + '_'
KEYWORD_CHARS = ascii_letters + digits + '_-'  # should accept ISO-10303-21 and lower case letters

STRING_CHARS = ascii_letters + digits + ' _' + SPECIAL + BACKSLASH
FIRST_NUMBER_CHARS = '-+01234567890'
NUMBER_CHARS = FIRST_NUMBER_CHARS + '.eE'
FIRST_ENUM_CHARS = ascii_uppercase + '_.'
ENUM_CHARS = ascii_uppercase + digits + '_.'

ENUMERATION = re.compile(r'\.[A-Z_][A-Z0-9_]*\.')
REFERENCE = re.compile(r"[#]\d+")
KEYWORD = re.compile(r"(?:!|)[A-Z_][0-9A-Za-z_]*")  # allow lowercase letters


class ParseError(Exception):
    pass


class StringDecodingError(ParseError):
    pass


class StepFileStructureError(Exception):
    pass


class ParameterList(tuple):
    """ Typing helper class for parameter list. """

    # list: (arg1, list2, ...)
    #
    # The elements of aggregates (SET, BAG, LIST, ARRAY) are given in parentheses, separated by ",".
    def __str__(self):
        return '({})'.format(','.join(parameter_string(p) for p in self))


AnyList = Union[Tuple, List, ParameterList]


class StructureToken(str):
    """ Typing helper class for ';', ',', '(', ')', '='. """
    pass


class Reference(str):
    """ Typing helper class for entity instance name."""
    pass


class Keyword(str):
    """ Typing helper class for keyword."""
    pass


class UserKeyword(Keyword):
    """ Typing helper class for user keyword."""
    pass


class Enumeration(str):
    """ Typing helper class for enumeration."""
    pass


class UnsetParameter(str):
    """ Typing helper class for unset parameter. """
    pass


class TypedParameter:
    """ Typed parameter, `type_name` is the type of the parameter, `param` is the parameter itself. """

    def __init__(self, name: str, param):
        self.type_name = Keyword(name)
        self.param = param

    def __str__(self):
        return f'{self.type_name}({parameter_string(self.param)})'


class Binary:
    """ Binary type for exporting, loaded binary data is converted to `int` automatically. """

    def __init__(self, value: int, unused: int = 0):
        self.value: int = value
        self.unused: int = unused

    def __str__(self):
        return '"{}{:X}"'.format(self.unused, self.value)


class Entity:
    """ STEP-file entity, `name` is the type of the entity, `params` are the entity parameters as a
    :class:`ParameterList`.
    """

    def __init__(self, name: str, params: AnyList):
        self.name = Keyword(name)
        self.params = ParameterList(params or tuple())

    def __str__(self):
        return self.name + parameter_string(self.params)


class EntityInstance:
    def __init__(self, ref: str):
        self.ref = Reference(ref)


class SimpleEntityInstance(EntityInstance):
    """ Simple instance entity, `ref` is the instance name as string (e.g. ``'#100'``), `entity` is the :class:`Entity`
    object.
    """

    def __init__(self, ref: str, entity: Entity):
        super().__init__(ref)
        self.entity = entity

    def __str__(self):
        return f"{self.ref}={str(self.entity)}{END_OF_INSTANCE}"


class ComplexEntityInstance(EntityInstance):
    """ A complex entity instance consist of multiple :class:`Entity` objects, `ref` is the instance name as string
    (e.g. ``'#100'``)
    """

    def __init__(self, ref: str, entities: List[Entity]):
        super().__init__(ref)
        self.entities = entities or list()

    def __str__(self):
        estr = "".join(str(e) for e in self.entities)
        return f"{self.ref}=({estr}){END_OF_INSTANCE}"


class HeaderSection:
    """

    The HEADER section has a fixed structure consisting of 3 to 6 groups in the given order. Except for the data fields
    time_stamp and FILE_SCHEMA all fields may contain empty strings.

    """
    REQUIRED_HEADER_ENTITIES = ('FILE_DESCRIPTION', 'FILE_NAME', 'FILE_SCHEMA')
    OPTIONAL_HEADER_ENTITIES = ('FILE_POPULATION', 'SECTION_LANGUAGE', 'SECTION_CONTENT')
    KNOWN_HEADER_ENTITIES = set(REQUIRED_HEADER_ENTITIES) | set(OPTIONAL_HEADER_ENTITIES)

    def __init__(self, entities: Dict = None):
        self.entities: Dict[str: Entity] = entities or OrderedDict()

    def add(self, entity: Entity) -> None:
        """ Add or replace header entry. """
        self.entities[entity.name] = entity

    def __getitem__(self, name: str) -> Entity:
        """ Returns header entry by `name`, raise :class:`KeyError` if not found. """
        return self.entities[name]

    def get(self, name: str) -> Optional[Entity]:
        """ Returns header entry by `name` or ``None`` if not found. """
        try:
            return self.entities[name]
        except KeyError:
            return None

    def set_file_description(self, description: Tuple = None, level: str = '2;1') -> None:
        description = ParameterList(description) if description else ParameterList()
        self.add(Entity('FILE_DESCRIPTION', ParameterList((
            ParameterList(description), str(level)
        ))))

    def set_file_name(self, name: str,
                      time_stamp: str = None,
                      author: str = '',
                      organization: Tuple = None,
                      preprocessor_version: Tuple = None,
                      organization_system: str = '',
                      autorization: str = '',
                      ) -> None:
        if time_stamp is None:
            time_stamp = datetime.utcnow().isoformat(timespec='seconds')

        organization = ParameterList(organization) if organization else ParameterList(('',))
        preprocessor_version = ParameterList(preprocessor_version) if preprocessor_version else ParameterList(('',))

        self.add(Entity('FILE_NAME', ParameterList((
            str(name),
            time_stamp,
            author,
            organization,
            preprocessor_version,
            organization_system,
            autorization,
        ))))

    def set_file_schema(self, schema: Tuple) -> None:
        schema = ParameterList((schema,)) if schema else ParameterList()
        self.add(Entity('FILE_SCHEMA', schema))

    def write(self, fp: TextIO) -> None:
        def write_entities(names, optional=False):
            for name in names:
                try:
                    entity = self[name]
                except KeyError:
                    if not optional:
                        raise StepFileStructureError(f'Missing required header entity: {name}')
                else:
                    fp.write(str(entity))
                    fp.write(END_OF_INSTANCE)

        fp.write('HEADER' + END_OF_INSTANCE)
        write_entities(names=HeaderSection.REQUIRED_HEADER_ENTITIES, optional=False)
        write_entities(names=HeaderSection.OPTIONAL_HEADER_ENTITIES, optional=True)
        fp.write('ENDSEC' + END_OF_INSTANCE)

        unknown_header_entities = set(self.entities.keys()) - HeaderSection.KNOWN_HEADER_ENTITIES
        if len(unknown_header_entities):
            raise StepFileStructureError(f'Found unsupported header entities: {unknown_header_entities}')


class DataSection:
    """
    The DATA section contains application data according to one specific express schema. The encoding of this data
    follows some simple principles.

    """

    def __init__(self, params: ParameterList = None, instances: Dict = None):
        self.parameter = params or ParameterList()
        self.instances: Dict[Reference, EntityInstance] = instances or OrderedDict()

    def __iter__(self):
        """ Returns iterable of all instances in this data section. """
        return self.instances.values()

    def add(self, instance: EntityInstance) -> None:
        """
        Append new entity `instance`. Replaces existing instances with same instance name if already exists.

        Args:
            instance: entity instance

        """
        self.instances[instance.ref] = instance

    def references(self) -> Iterable[Reference]:
        """ Returns iterable of entity instance names. """
        return self.instances.keys()

    def __getitem__(self, ref: str) -> EntityInstance:
        """ Returns instance by `ref`, raise :class:`KeyError` if not found. """
        return self.instances[ref]

    def __len__(self) -> int:
        """ Returns count of instances. """
        return len(self.instances)

    def get(self, ref: str) -> Optional[EntityInstance]:
        """ Returns instance by `ref` of ``None`` if not found. """
        try:
            return self.instances[ref]
        except KeyError:
            return None

    def write(self, fp: TextIO):
        fp.write('DATA')
        if len(self.parameter):
            fp.write(parameter_string(self.parameter))
        fp.write(END_OF_INSTANCE)
        for instance in self.instances.values():
            fp.write(str(instance))
        fp.write('ENDSEC' + END_OF_INSTANCE)


class StepFile:
    """ STEP physical file representation (STEP-file).

    A STEP-File has one :class:`HeaderSection`, and at least one :class:`DataSection`.

    """

    def __init__(self):
        self.header = HeaderSection()
        # multiple data sections only supported by ISO 10303-21:2002
        # most files in the wild, don't use multiple data sections!
        self.data: List[DataSection] = list()
        self._linked_data_sections: ChainMap = None

    def __getitem__(self, ref: str):
        """ Returns :class:`EntityInstance` by instance name `ref`. Searches all data sections if more than one exist.

        Args:
            ref: entity instance name as string e.g. ``'#100'``

        Raises:
              KeyError: instance `id` not found

        """
        if self._linked_data_sections is None:
            self._rebuild_chain_map()
        return self._linked_data_sections[ref]

    def __len__(self) -> int:
        """ Returns count of all stored entity instances. """
        return len(self._linked_data_sections)

    def __iter__(self) -> Iterable[EntityInstance]:
        """ Returns iterable of all instance entities of all data sections."""
        for ds in self.data:
            yield from ds.instances.values()

    def get(self, ref: Reference) -> Optional[EntityInstance]:
        """ Returns :class:`EntityInstance` by instance name `ref` or ``None`` if not found. Searches all data sections
        if more than one exist.

        Args:
            ref: entity instance name as string e.g. ``'#100'``

        """
        try:
            return self.__getitem__(ref)
        except KeyError:
            return None

    def _rebuild_chain_map(self) -> None:
        """ Rebuild chain map for searching across multiple data sections.
        """
        self._linked_data_sections = ChainMap(*[ds.instances for ds in self.data])

    def append(self, data: DataSection) -> None:
        """
        Append new data section `data`.

        Args:
            data: data section

        """
        self.data.append(data)
        self._rebuild_chain_map()

    def new_data_section(self, params: Iterable = None) -> DataSection:
        """ Create a new :class:`DataSection` and append to existing data sections. """
        params = ParameterList(params) if params else ParameterList()
        new_section = DataSection(params=params)
        self.append(new_section)
        return new_section

    def write(self, fp: TextIO) -> None:
        """
        Serialize to a STEP-file (ISO 10303-21) formatted stream to ``fp`` (a :meth:`write`-supporting
        file-like object).

        File encoding should be ``'iso-8859-1'`` but can also be ``'ascii'``, because ISO 10303-21 requires special encoding
        for characters > 126 into characters < 127 as unicode compatible characters, which should be compatible with most
        encodings, but don't use 16-bit encodings!

        Args:
            fp: text stream
        """
        fp.write('ISO-10303-21' + END_OF_INSTANCE)
        self.header.write(fp)
        for data in self.data:
            data.write(fp)
        fp.write('END-ISO-10303-21' + END_OF_INSTANCE)

    def save(self, name: str) -> None:
        """ Export STEP-file to the file system. """
        with open(name, mode='wt', encoding=STEP_FILE_ENCODING) as fp:
            self.write(fp)

    def __str__(self) -> str:
        """
        Serialize to a STEP-file (ISO 10303-21) formatted ``str``.

        Special encoding for characters > 126 into characters < 127 as unicode compatible characters according to
        ISO 10303-21 standard will be applied.

        """
        fp = StringIO()
        self.write(fp)
        s = fp.getvalue()
        fp.close()
        return s

    def has_reference(self, ref: str) -> bool:
        """ Returns `True` if reference `ref` exist in any data section. """
        return ref in self._linked_data_sections


ASCII_ONLY_ENCODED_PARAMETERS = {Enumeration, Keyword, Reference, UnsetParameter}


def _to_unicode(s, l, t) -> str:
    return ''.join(chr(int(hexstr, 16)) for hexstr in t[1:-1])


def quoted_string(s: str) -> str:
    return f"'{step_string_encoder(s)}'"


def parameter_string(p) -> str:
    if p is None:
        return '$'
    type_ = type(p)
    if type_ in ASCII_ONLY_ENCODED_PARAMETERS:
        # faster without step encoding
        return p
    elif type_ is str:  # quote with apostrophe
        return quoted_string(p)
    # tuple, list, ParameterList, TypedParameter, float, int, Binary
    if isinstance(p, (tuple, list)):
        p = ParameterList(p)
    # TODO: floats may need special treatment for exponential floats like 1e-10 -> 1E-10
    return str(p)


HEX_16BIT = "{:04X}"
HEX_32BIT = "{:08X}"
EXT_START_16 = '\\X2\\'
EXT_START_32 = '\\X4\\'
EXT_END = "\\X0\\"
EXT_ENCODING = {
    16: HEX_16BIT,
    32: HEX_32BIT,
}


def step_string_encoder(s: str) -> str:
    buffer = []
    encoding = 0  # 0 for no encoding, 16 for 16bit encoding, 32 for 32bit encoding
    for char in s:
        value = ord(char)
        if value < 127:  # just ASCII code
            if encoding:  # stop extended encoding
                buffer.append(EXT_END)
                encoding = 0
            if char == '\\':  # escaping backslash
                char = '\\\\'
            elif char == "'":  # escaping apostrophe
                char = "''"
            buffer.append(char)
        else:  # value > 126
            if not encoding:  # start new extended character sequence
                if value < 65536:  # 16bit character
                    encoding = 16
                    buffer.append(EXT_START_16)
                else:  # 32bit character
                    encoding = 32
                    buffer.append(EXT_START_32)
            elif value >= 65536 and encoding == 16:
                # already extended 16bit encoding, but 32bit encoding is required
                # stop 16bit encoding
                buffer.append(EXT_END)
                # and start 32bit encoding
                encoding = 32
                buffer.append(EXT_START_32)
            buffer.append(EXT_ENCODING[encoding].format(value))
    if encoding:
        buffer.append(EXT_END)
    return ''.join(buffer)


# control_directive = page | alphabet | extended2 | extended4 | arbitrary .
# page = '\S\'  character  - not supported
# alphabet = '\P' upper '\'  - not supported
# arbitrary = '\X\' hex_one - not supported
# extended2 ='\X2\' HEX_16BIT { HEX_16BIT } EXT_END
# extended2 ='\X4\' HEX_32BIT { HEX_32BIT } EXT_END

EXT_MATCH = re.compile(r'\\(X[24])\\([0-9A-F]+)\\X0\\')


def _decode_bytes(ext_type: str, hexstr: str) -> str:
    if ext_type == 'X2':
        hex_char_count = 4
    else:
        hex_char_count = 8
    length = len(hexstr)
    if length % hex_char_count:
        raise StringDecodingError
    chars = []
    start = 0

    while start < length:
        char = chr(int(hexstr[start:start + hex_char_count], 16))
        chars.append(char)
        start += hex_char_count
    return ''.join(chars)


def step_string_decoder(s: str) -> str:
    origin = s
    while True:
        r = EXT_MATCH.search(s)
        if r is None:
            break
        try:
            decoded_chars = _decode_bytes(r[1], r[2])
        except StringDecodingError:
            raise StringDecodingError(f'Invalid extended encoding in string "{origin}".')
        s = s.replace(r[0], decoded_chars)
    return s.replace('\\\\', '\\')


class Buffer:
    def __init__(self, buffer: str):
        self._buffer = buffer
        self._cursor = 0
        self.line_number = 1

    def look(self, n=0):
        try:
            return self._buffer[self._cursor + n]
        except IndexError:
            self._cursor = len(self._buffer)
            return EOF

    def get(self):
        value = self.look()
        if value == '\n':
            self.line_number += 1
        self._cursor += 1
        return value

    def skip(self, n=1):
        self._cursor += n


class Lexer:
    DEFAULT = 0
    STRING = 1
    COMMENT = 2

    def __init__(self, s: str):
        self.buffer = Buffer(s)

    def __iter__(self):
        return self.parse()

    @property
    def line_number(self):
        return self.buffer.line_number

    def parse(self) -> Iterable[str]:
        current = self.buffer.look()
        while current != EOF:
            if current <= ' ':
                # skip white space, tabs, new line ....
                self.buffer.get()
            elif current == '/' and self.buffer.look(1) == '*':
                self.comment()
            elif current in SINGLE_CHAR_TOKENS:
                char = self.buffer.get()
                if char in '*$':
                    char = UnsetParameter(char)
                else:
                    char = StructureToken(char)
                yield char
            elif current in FIRST_KEYWORD_CHAR:
                yield Keyword(self.keyword())
            elif current == APOSTROPHE:
                yield step_string_decoder(self.string())  # str
            elif current == '#':
                yield Reference(self.reference())
            elif current == '!':
                yield UserKeyword(self.keyword())
            elif current in FIRST_NUMBER_CHARS:
                yield self.number()  # int or float
            elif current == '.' and self.buffer.look(1) in FIRST_ENUM_CHARS:
                yield Enumeration(self.enum())
            elif current == '"' and self.buffer.look(1) in '0123':
                yield self.binary()  # int
            else:
                raise ParseError(f'Unexpected character {current} in line {self.buffer.line_number}.')
            current = self.buffer.look()

    def comment(self):
        """ Skip comments."""
        b = self.buffer
        b.skip(2)
        current = b.look()
        while True:
            if current == '*' and b.look(1) == '/':
                b.skip(2)
                return
            elif current == EOF:
                raise ParseError('Missing end of comment, got unexpected end of file.')
            else:
                b.get()
                current = b.look()

    def string(self) -> str:
        """ Return string without quotes. """
        b = self.buffer
        s = []
        b.skip()
        while True:
            current = b.look()
            if current == APOSTROPHE:
                if b.look(1) == APOSTROPHE:
                    # apostrophe decoding has to be done by the lexer
                    b.skip(2)
                    s.append(APOSTROPHE)
                else:
                    b.skip()
                    return ''.join(s)
            elif current in STRING_CHARS:
                s.append(b.get())
            else:
                raise ParseError(f'Found invalid character in string "{current}".')

    def binary(self):
        b = self.buffer
        s = []
        b.skip(2)
        while True:
            current = b.look()
            if current in hexdigits:
                s.append(b.get())
            elif current == '"':
                b.get()
                return int(''.join(s), 16)
            else:
                raise ParseError(f'Found invalid binary in line {b.line_number}.')

    def number(self):
        b = self.buffer
        s = []
        is_real = False
        while True:
            current = b.look()
            if current in NUMBER_CHARS:
                if current in '.eE':
                    is_real = True
                s.append(b.get())
            else:
                break

        nstr = ''.join(s)
        try:
            if is_real:
                return float(nstr)
            else:
                return int(nstr)
        except ValueError:
            raise ParseError(f'Found invalid number "{nstr}" in line {b.line_number}.')

    def enum(self):
        b = self.buffer
        s = [b.get(), b.get()]
        while True:
            current = b.look()
            if current in ENUM_CHARS:
                s.append(b.get())
                if current == '.':
                    return ''.join(s)
            else:
                estr = ''.join(s)
                raise ParseError(f'Found invalid enum "{estr}" in line {b.line_number}.')

    def keyword(self) -> str:
        b = self.buffer
        s = [b.get()]
        while True:
            if b.look() in KEYWORD_CHARS:
                s.append(b.get())
            else:
                return ''.join(s)

    def reference(self) -> str:
        """ References: #1234 """
        b = self.buffer
        s = [b.get()]
        while True:
            if b.look() in digits:
                s.append(b.get())
            else:
                return ''.join(s)


PARAMETER_TYPES = {int, float, str, Enumeration, UnsetParameter, Reference}


class Parser:
    def __init__(self, lexer):
        self.tokens = list(lexer)
        self.tokens.reverse()
        self.current_instance = None

    @property
    def lookahead(self):
        try:
            return self.tokens[-1]
        except IndexError:
            return None

    def pop(self):
        try:
            return self.tokens.pop()
        except IndexError():
            raise ParseError('Unexpected end of file.')

    def _keyword(self):
        if KEYWORD.fullmatch(self.lookahead):
            return self.pop()
        else:
            raise ParseError(f'Invalid keyword: {self.lookahead}')

    def _typed_param(self) -> TypedParameter:
        name = self._keyword()
        if self.pop() != '(':
            raise ParseError(
                f'Expected "(" after type for typed parameter: {name} in instance: {self.current_instance}.')
        if self.lookahead == '(':
            param = self._parameter_list()
        else:
            param = self.pop()
            if type(param) not in PARAMETER_TYPES:
                raise ParseError(
                    f'Expected parameter type for typed parameter: {name} in instance: {self.current_instance}.')

        if self.pop() != ')':
            raise ParseError(f'Expected ")" after typed parameter: {name} in instance: {self.current_instance}.')
        return TypedParameter(name, param)

    def _parameter_list(self) -> ParameterList:
        if self.pop() != '(':
            raise ParseError('Expected "(" for parameter list.')
        if self.lookahead == ')':  # empty list
            self.pop()
            return ParameterList()
        params = []
        while True:
            if self.lookahead == '(':
                param = self._parameter_list()
            elif isinstance(self.lookahead, Keyword):
                param = self._typed_param()
            elif type(self.lookahead) in PARAMETER_TYPES:
                param = self.pop()
            else:
                raise ParseError(
                    f'Unexpected parameter "{self.lookahead}" in parameter list in instance: {self.current_instance}.')
            params.append(param)
            if self.lookahead == ')':
                self.pop()
                return ParameterList(params)
            elif self.pop() != ',':
                raise ParseError('Expected "," between parameters in parameter list.')

    def _entity(self) -> Entity:
        name = self._keyword()
        if self.lookahead == '(':  # optional parameter list
            params = self._parameter_list()
        else:
            params = None
        return Entity(name=name, params=params)

    def _instance(self) -> EntityInstance:
        instance_id = self.tokens.pop()
        if not isinstance(instance_id, Reference):
            raise ParseError(f'Invalid reference: {instance_id}.')
        self.current_instance = instance_id
        if self.pop() != '=':
            raise ParseError(f'Expected "=" after reference: {instance_id}')

        if self.lookahead == '(':  # Complex Instance Entity
            self.pop()  # (
            entities = list()
            while self.lookahead != ')':
                entity = self._entity()
                entities.append(entity)
            self.pop()  # )
            if self.pop() != ';':
                raise ParseError(f'Expected: ";" after complex entity instance: {instance_id}')

            return ComplexEntityInstance(ref=instance_id, entities=entities)
        else:
            entity = self._entity()
            if self.pop() != ';':
                raise ParseError(f'Expected: ";" after simple entity instance: {instance_id}.')
            return SimpleEntityInstance(ref=instance_id, entity=entity)

    def _header(self) -> HeaderSection:
        header = HeaderSection()
        if self.pop() != 'HEADER' or self.pop() != ';':
            raise ParseError('Expected: HEADER; section')

        while self.lookahead != 'ENDSEC':
            entity = self._entity()
            if self.lookahead == ';':
                self.pop()
            else:
                raise ParseError(f'Expected: ";" after HEADER entry: {entity.name}.')
            header.add(entity)
        self.pop()  # ENDSEC
        if self.pop() != ';':
            raise ParseError('Expected: ";" after ENDSEC')
        return header

    def _data_section(self) -> DataSection:
        data = DataSection()
        if self.pop() != 'DATA':
            raise ParseError('Expected: DATA section')
        # optional parameter list of data section: DATA(arg1, list1, ...)
        if isinstance(self.lookahead, ParameterList):
            data.parameter = self.pop()
        else:
            if self.pop() != ';':
                raise ParseError('Expected: ";" after DATA')

        while self.lookahead != 'ENDSEC':
            instance = self._instance()
            data.add(instance)
        self.pop()  # ENDSEC
        if self.pop() != ';':
            raise ParseError('Expected: ";" after ENDSEC')
        return data

    def parse(self) -> 'StepFile':
        step = StepFile()

        assert self.pop() == 'ISO-10303-21'
        assert self.pop() == ';'

        step.header = self._header()
        while self.lookahead != 'END-ISO-10303-21':
            # multiple data sections support
            step.append(self._data_section())

        assert self.pop() == 'END-ISO-10303-21'
        assert self.pop() == ';'

        return step


# Public Interface

def timestamp() -> str:
    """ Factory function returns an ISO formatted UTC timestamp. """
    return datetime.utcnow().isoformat(timespec='seconds')


def is_string(e) -> bool:
    """ Returns ``True`` if `e` is a ``str``. """
    return type(e) is str


def is_integer(e) -> bool:
    """ Returns ``True`` if `e` is an ``int``. """
    return type(e) is int


def is_real(e) -> bool:
    """ Returns ``True`` if `e` is a ``float``. """
    return type(e) is float


def is_binary(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`Binary`. """
    return type(e) is Binary


def is_reference(e) -> bool:
    """ Returns ``True`` if `e` is an :class:`EntityInstanceName`. """
    return type(e) is Reference


def is_keyword(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`Keyword`. """
    return type(e) is Keyword


def is_enum(e) -> bool:
    """ Returns ``True`` if `e` is an :class:`Enumeration`. """
    return type(e) is Enumeration


def is_unset_parameter(e) -> bool:
    """ Returns ``True`` if `e` is an unset or omitted parameter (:class:`UnsetParameter`). """
    return type(e) is UnsetParameter


def is_typed_parameter(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`TypedParameter`. """
    return type(e) is TypedParameter


def is_parameter_list(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`ParameterList`. """
    return type(e) is ParameterList


def is_entity(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`Entity`. """
    return type(e) is Entity


def is_simple_entity_instance(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`SimpleEntityInstance`. """
    return type(e) is SimpleEntityInstance


def is_complex_entity_instance(e) -> bool:
    """ Returns ``True`` if `e` is a :class:`ComplexEntityInstance`. """
    return type(e) is ComplexEntityInstance


def keyword(name: str) -> Keyword:
    """ Factory function to create a new :class:`Keyword` object. Only uppercase letters an digits are allowed,
    standard keyword has to start with an uppercase letter an user defined keyword has to start with ``'!'``.
    """
    if KEYWORD.fullmatch(name):
        return Keyword(name)
    else:
        raise ValueError(f'Invalid formed keyword: {name}')


def reference(ref: str) -> Reference:
    """ Factory function to create a new :class:`Reference` object (Entity Instance Name). A reference has to start
    with ``'#'`` followed by only digits e.g. ``'#100'``
    """
    if REFERENCE.fullmatch(ref):
        return Reference(ref)
    else:
        raise ValueError(f'Invalid formed reference: {ref}')


def enum(enum: str) -> Enumeration:
    """ Factory function to create a new :class:`Enumeration` object. A enumeration is surrounded ``'.'`` and only
    uppercase letters and digits are allowed e.g. ``'.TRUE.'`` or ``'.FALSE.'``.
    """
    if ENUMERATION.fullmatch(enum):
        return Enumeration(enum)
    else:
        raise ValueError(f'Invalid formed enumeration: {enum}')


def binary(value: int, unset: int = 0) -> Binary:
    """ Factory function to create a new :class:`Binary` object. Only for export used, `unset` specifies the
    uppermost unset bits.
    """
    if unset not in (0, 1, 2, 3):
        raise ValueError('Argument `unset` has to be in  range from 0 to 3.')
    return Binary(int(value), unset)


def unset_parameter(char: str) -> UnsetParameter:
    """ Factory function to create a new :class:`UnsetParameter` object. Unset attribute values are given
    as ``'$'``. Explicit attributes which got re-declared as derived in a subtype are encoded as ``'*'`` in the
    position of the supertype attribute.
    """
    if char not in '*$':
        raise ValueError(f'Invalid character for unset parameter: "{char}"')
    return UnsetParameter(char)


def parameter_list(*args) -> ParameterList:
    """ Factory function to create a new :class:`ParameterList` object. """
    return ParameterList(args)


def typed_parameter(type_name: str, param) -> TypedParameter:
    """ Factory function to create a new :class:`TypedParameter` object.

    Args:
         type_name: type name as ``str`` or :class:`Keyword` object.
         param: typed parameter
    """
    return TypedParameter(keyword(type_name), param)


def entity(name: str, params: AnyList) -> Entity:
    """ Factory function to create a new :class:`Entity` object.

    Args:
         name: entity name as str or :class:`Keyword` object
         params: entity parameters as ``tuple``, ``list`` or :class:`ParameterList`

    """
    return Entity(keyword(name), params)


def simple_entity_instance(ref: str, entity: Entity) -> SimpleEntityInstance:
    """ Factory function to create a new :class:`SimpleEntityInstance` object.

    Args:
        ref: instance reference as ``str`` or :class:`Reference` object.
        entity: entity as :class:`Entity` object
    """
    return SimpleEntityInstance(reference(ref), entity)


def simple_instance(ref: str, name: str, params: AnyList) -> SimpleEntityInstance:
    """ Factory function to create a new :class:`SimpleEntityInstance` object. This method creates the
    :class:`Entity` object automatically.

    Args:
        ref: instance reference as ``str`` or :class:`Reference` object.
        name: entity name as str or :class:`Keyword` object
        params: entity parameters as ``tuple``, ``list`` or :class:`ParameterList`

    """
    return SimpleEntityInstance(reference(ref), entity(name, params))


def complex_entity_instance(ref: str, entities: List[Entity]) -> ComplexEntityInstance:
    """ Factory function to create a new :class:`ComplexEntityInstance` object.

    Args:
        ref: instance reference as ``str`` or :class:`Reference` object.
        entities: list of :class:`Entity` objects.

    """
    for entity in entities:
        if not is_entity(entity):
            raise ValueError('Only Entity() types allowed.')
    return ComplexEntityInstance(reference(ref), entities)


def new_step_file() -> StepFile:
    """ Factory function to create a new :class:`StepFile` object. """
    return StepFile()


def loads(s: str) -> StepFile:
    """ Load STEP-file (ISO 10303-21) from unicode string.

    Decoding for special characters > 126 to unicode characters according to ISO 10303-21 standard will
    be applied.

    Args:
        s: STEP-file content as unicode string

    """
    lexer = Lexer(s)
    return Parser(lexer).parse()


def load(fp: TextIO) -> StepFile:
    """ Load STEP-file (ISO 10303-21) from text stream.

    A special encoding form characters > 126 is applied in STEP-Files, therefore an encoding setting at opening files
    is not necessary, reading as ``'ascii'`` works fine. Decoding of this special characters will be applied.

    Args:
        fp: STEP-file content as text stream yielding unicode strings

    """
    content = fp.read()
    return loads(content)


def readfile(filename: str) -> StepFile:
    """ Read STEP-file (ISO 10303-21) `filename` from file system. """
    with open(filename, 'rt', encoding=STEP_FILE_ENCODING) as fp:
        return load(fp)
