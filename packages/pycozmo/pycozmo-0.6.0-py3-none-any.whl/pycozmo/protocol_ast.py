"""

Protocol AST.

"""

import enum
from abc import ABC
from typing import List, Optional, Union


class FrameType(enum.Enum):
    RESET = 1
    RESET_ACK = 2
    FIN = 3
    ENGINE_ACT = 4
    ENGINE = 7
    ROBOT = 9
    PING = 0x0b


class PacketType(enum.Enum):
    UNKNOWN = -1
    CONNECT = 2
    DISCONNECT = 3
    COMMAND = 4
    EVENT = 5
    KEYFRAME = 0x0a
    PING = 0x0b


class Argument(ABC):
    """ Base class for packet arguments. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None):
        self.name = str(name) if name else None
        self.description = str(description) if description else None

    def type_hint(self) -> Optional[str]:
        return None


class FloatArgument(Argument):
    """ 32-bit floating point number. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: float = 0.0):
        super().__init__(name, description)
        self.default = float(default)

    def type_hint(self):
        return "float"


class DoubleArgument(Argument):
    """ 64-bit floating point number. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: float = 0.0):
        super().__init__(name, description)
        self.default = float(default)

    def type_hint(self):
        return "double"


class BoolArgument(Argument):
    """ 8-bit boolean. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: bool = False):
        super().__init__(name, description)
        self.default = bool(default)

    def type_hint(self):
        return "bool"


class UIntArgument(Argument, ABC):
    """ Base class for unsigned integers. """


class UInt8Argument(UIntArgument):
    """ 8-bit unsigned integer. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: int = 0):
        super().__init__(name, description)
        self.default = int(default)

    def type_hint(self):
        return "uint8"


class UInt16Argument(UIntArgument):
    """ 16-bit unsigned integer. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: int = 0):
        super().__init__(name, description)
        self.default = int(default)

    def type_hint(self):
        return "uint16"


class UInt32Argument(UIntArgument):
    """ 32-bit unsigned integer. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: int = 0):
        super().__init__(name, description)
        self.default = int(default)

    def type_hint(self):
        return "uint32"


class IntArgument(Argument, ABC):
    """ Base class for signed integers. """


class Int8Argument(IntArgument):
    """ 8-bit signed integer. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: int = 0):
        super().__init__(name, description)
        self.default = int(default)

    def type_hint(self):
        return "int8"


class Int16Argument(IntArgument):
    """ 16-bit signed integer. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: int = 0):
        super().__init__(name, description)
        self.default = int(default)

    def type_hint(self):
        return "int16"


class Int32Argument(IntArgument):
    """ 32-bit signed integer. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, default: int = 0):
        super().__init__(name, description)
        self.default = int(default)

    def type_hint(self):
        return "int32"


class EnumMember(object):
    """ Base class for enumeration members. """

    def __init__(self, name: str, value: int, description: Optional[str] = None):
        self.name = str(name)
        self.description = str(description) if description else None
        self.value = int(value)


class Enum(object):
    """ Base class for enumerations. """

    def __init__(self, name: str, description: Optional[str] = None,
                 members: Optional[List[EnumMember]] = None, base: int = 10):
        self.name = str(name)
        self.description = str(description) if description else None
        self.members = list(members) if members else []
        self.base = int(base)


class EnumArgument(Argument):
    """ Base class for enumeration arguments. """

    def __init__(self, name: str, enum_type: Enum, description: Optional[str] = None,
                 data_type: Union[IntArgument, UIntArgument] = Int8Argument(),
                 default=0):
        super().__init__(name, description)
        self.enum_type = enum_type
        self.data_type = data_type
        self.default = default

    def type_hint(self):
        return self.enum_type.name


class Struct(object):
    """ Base class for structures. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None,
                 arguments: Optional[List[Argument]] = None):
        self.name = str(name) if name else None
        self.description = str(description) if description else None
        self.arguments = list(arguments) if arguments else []


class FArrayArgument(Argument):
    """ Fixed-length array. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None,
                 data_type: Union[Argument, Struct] = UInt8Argument(), length: int = 0, default=()):
        super().__init__(name, description)
        self.data_type = data_type
        self.length = length
        self.default = tuple(default)

    def type_hint(self):
        if isinstance(self.data_type, Struct):
            type_name = self.data_type.name
        else:
            type_name = self.data_type.type_hint()
        return "{}[{}]".format(type_name, self.length)


class VArrayArgument(Argument):
    """ Variable-length array. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None,
                 data_type: Argument = UInt8Argument(), length_type: Argument = UInt16Argument(), default=()):
        super().__init__(name, description)
        self.data_type = data_type
        self.length_type = length_type
        self.default = tuple(default)

    def type_hint(self):
        data_type_name = self.data_type.type_hint()
        length_type_name = self.length_type.type_hint()
        return "{}[{}]".format(data_type_name, length_type_name)


class StringArgument(Argument):
    """ String. """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None,
                 length_type: Argument = UInt16Argument(), default=""):
        super().__init__(name, description)
        self.length_type = length_type
        self.default = str(default)

    def type_hint(self):
        return "str"


class Packet(Struct, ABC):
    """ Base class for packets. """

    def __init__(self, packet_type: PacketType, name: str, packet_id: Optional[int] = None,
                 group: Optional[str] = None, description: Optional[str] = None,
                 arguments: Optional[List[Argument]] = None):
        super().__init__(name, description, arguments)
        self.type = PacketType(packet_type)
        self.id = packet_id
        self.group = group


class Connect(Packet):
    """ Connection acknowledgement packet. """

    def __init__(self):
        super().__init__(PacketType.CONNECT, "Connect")


class Disconnect(Packet):
    """ Disconnect packet. """

    def __init__(self):
        super().__init__(PacketType.DISCONNECT, "Disconnect")


class Command(Packet):
    """ Command packet. """

    def __init__(self, packet_id: int, name: str, group: Optional[str] = None,  description: Optional[str] = None,
                 arguments: Optional[List[Argument]] = None):
        super().__init__(PacketType.COMMAND, name, packet_id=packet_id, group=group, description=description,
                         arguments=arguments)


class Event(Packet):
    """ Event packet. """

    def __init__(self, packet_id: int, name: str, group: Optional[str] = None, description: Optional[str] = None,
                 arguments: Optional[List[Argument]] = None):
        super().__init__(PacketType.EVENT, name, packet_id=packet_id, group=group, description=description,
                         arguments=arguments)


class Ping(Packet):
    """ Ping packet. """

    def __init__(self):
        super().__init__(PacketType.PING, "Ping", arguments=[
            DoubleArgument("time_sent_ms"),
            UInt32Argument("counter"),
            UInt32Argument("last"),
            UInt8Argument("unknown"),
        ])


class Keyframe(Packet):

    def __init__(self):
        super().__init__(PacketType.KEYFRAME, "Keyframe")


class Protocol(object):
    """ Protocol declaration. """

    def __init__(self, enums: List[Enum], structs: List[Struct], packets: List[Packet]):
        self.enums = list(enums)
        self.structs = list(structs)
        self.packets = list(packets)
