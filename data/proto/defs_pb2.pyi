from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SymbolInfoStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID_SYMBOL_INFO_STATUS: _ClassVar[SymbolInfoStatus]
    ADD: _ClassVar[SymbolInfoStatus]
    REMOVE: _ClassVar[SymbolInfoStatus]
    UPDATE: _ClassVar[SymbolInfoStatus]

class Side(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID_SIDE: _ClassVar[Side]
    BUY: _ClassVar[Side]
    SELL: _ClassVar[Side]

class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID_ORDERTPYE: _ClassVar[OrderType]
    MARKET: _ClassVar[OrderType]
    LIMIT: _ClassVar[OrderType]
    STOP: _ClassVar[OrderType]
    STOP_LIMIT: _ClassVar[OrderType]
    STOPLIMIT: _ClassVar[OrderType]

class Session(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL: _ClassVar[Session]
    AM: _ClassVar[Session]
    PM: _ClassVar[Session]
    SEAMLESS: _ClassVar[Session]

class Duration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID_DURATION: _ClassVar[Duration]
    DAY: _ClassVar[Duration]
    GTC: _ClassVar[Duration]
    GOOD_TILL_CANCEL: _ClassVar[Duration]
    FILL_OR_KILL: _ClassVar[Duration]
    FOK: _ClassVar[Duration]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID_STATUS: _ClassVar[Status]
    QUEUED: _ClassVar[Status]
    WORKING: _ClassVar[Status]
    FILLED: _ClassVar[Status]
    PENDING_CANCEL: _ClassVar[Status]
    CANCELED: _ClassVar[Status]
    PENDING_REPLACE: _ClassVar[Status]
    REPLACED: _ClassVar[Status]
    REPLACE_REJECT: _ClassVar[Status]
    INTERNAL_REJECT: _ClassVar[Status]
    CANCEL_REJECT: _ClassVar[Status]
    REJECT: _ClassVar[Status]
    REJECTED: _ClassVar[Status]
    PENDING_ACTIVATION: _ClassVar[Status]
    AWAITING_UR_OUT: _ClassVar[Status]
    PARTIAL_FILLED: _ClassVar[Status]
    REINSTATE: _ClassVar[Status]
    AWAITING_PARENT_ORDER: _ClassVar[Status]
    AWAITING_CONDITION: _ClassVar[Status]
    AWAITING_MANUAL_REVIEW: _ClassVar[Status]
    ACCEPTED: _ClassVar[Status]
    EXPIRED: _ClassVar[Status]

class OrderStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SINGLE: _ClassVar[OrderStrategyType]
    OCO: _ClassVar[OrderStrategyType]
    TRIGGER: _ClassVar[OrderStrategyType]

class SpecialInstruction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_SPECIAL_INSTRUCTION: _ClassVar[SpecialInstruction]
    AON: _ClassVar[SpecialInstruction]
    ALL_OR_NONE: _ClassVar[SpecialInstruction]
    DNR: _ClassVar[SpecialInstruction]
    DO_NOT_REDUCE: _ClassVar[SpecialInstruction]
    AON_DNR: _ClassVar[SpecialInstruction]
    ALL_OR_NONE_DO_NOT_REDUCE: _ClassVar[SpecialInstruction]

class RequestedDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_REQUESTED_DESTINATION: _ClassVar[RequestedDestination]
    INET: _ClassVar[RequestedDestination]
    ARCA: _ClassVar[RequestedDestination]
    ECN_ARCA: _ClassVar[RequestedDestination]
    CBOE: _ClassVar[RequestedDestination]
    AMEX: _ClassVar[RequestedDestination]
    PHLX: _ClassVar[RequestedDestination]
    ISE: _ClassVar[RequestedDestination]
    BOX: _ClassVar[RequestedDestination]
    NYSE: _ClassVar[RequestedDestination]
    NASDAQ: _ClassVar[RequestedDestination]
    BATS: _ClassVar[RequestedDestination]
    C2: _ClassVar[RequestedDestination]
    AUTO: _ClassVar[RequestedDestination]
    SIMEX: _ClassVar[RequestedDestination]
    PINK_SHEET: _ClassVar[RequestedDestination]
    PACIFIC: _ClassVar[RequestedDestination]
    OTCBB: _ClassVar[RequestedDestination]

class Marketability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NON_MARKETABLE: _ClassVar[Marketability]
    MARKETABLE: _ClassVar[Marketability]

INVALID_SYMBOL_INFO_STATUS: SymbolInfoStatus
ADD: SymbolInfoStatus
REMOVE: SymbolInfoStatus
UPDATE: SymbolInfoStatus
INVALID_SIDE: Side
BUY: Side
SELL: Side
INVALID_ORDERTPYE: OrderType
MARKET: OrderType
LIMIT: OrderType
STOP: OrderType
STOP_LIMIT: OrderType
STOPLIMIT: OrderType
NORMAL: Session
AM: Session
PM: Session
SEAMLESS: Session
INVALID_DURATION: Duration
DAY: Duration
GTC: Duration
GOOD_TILL_CANCEL: Duration
FILL_OR_KILL: Duration
FOK: Duration
INVALID_STATUS: Status
QUEUED: Status
WORKING: Status
FILLED: Status
PENDING_CANCEL: Status
CANCELED: Status
PENDING_REPLACE: Status
REPLACED: Status
REPLACE_REJECT: Status
INTERNAL_REJECT: Status
CANCEL_REJECT: Status
REJECT: Status
REJECTED: Status
PENDING_ACTIVATION: Status
AWAITING_UR_OUT: Status
PARTIAL_FILLED: Status
REINSTATE: Status
AWAITING_PARENT_ORDER: Status
AWAITING_CONDITION: Status
AWAITING_MANUAL_REVIEW: Status
ACCEPTED: Status
EXPIRED: Status
SINGLE: OrderStrategyType
OCO: OrderStrategyType
TRIGGER: OrderStrategyType
NO_SPECIAL_INSTRUCTION: SpecialInstruction
AON: SpecialInstruction
ALL_OR_NONE: SpecialInstruction
DNR: SpecialInstruction
DO_NOT_REDUCE: SpecialInstruction
AON_DNR: SpecialInstruction
ALL_OR_NONE_DO_NOT_REDUCE: SpecialInstruction
NO_REQUESTED_DESTINATION: RequestedDestination
INET: RequestedDestination
ARCA: RequestedDestination
ECN_ARCA: RequestedDestination
CBOE: RequestedDestination
AMEX: RequestedDestination
PHLX: RequestedDestination
ISE: RequestedDestination
BOX: RequestedDestination
NYSE: RequestedDestination
NASDAQ: RequestedDestination
BATS: RequestedDestination
C2: RequestedDestination
AUTO: RequestedDestination
SIMEX: RequestedDestination
PINK_SHEET: RequestedDestination
PACIFIC: RequestedDestination
OTCBB: RequestedDestination
NON_MARKETABLE: Marketability
MARKETABLE: Marketability
