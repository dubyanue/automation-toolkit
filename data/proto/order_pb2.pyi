import datetime
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2

from data.proto import defs_pb2 as _defs_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ()
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENTEREDTIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SIMEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FILLEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    CLORDID_FIELD_NUMBER: _ClassVar[int]
    ORDERVERSIONNUM_FIELD_NUMBER: _ClassVar[int]
    ORIGORDERID_FIELD_NUMBER: _ClassVar[int]
    ROOTORDERID_FIELD_NUMBER: _ClassVar[int]
    ORIGCLORDID_FIELD_NUMBER: _ClassVar[int]
    ROOTCLORDID_FIELD_NUMBER: _ClassVar[int]
    ORDERSTRATEGYTYPE_FIELD_NUMBER: _ClassVar[int]
    SPECIALINSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    BIDPX_FIELD_NUMBER: _ClassVar[int]
    ASKPX_FIELD_NUMBER: _ClassVar[int]
    SENDERSUBID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    STOPPRICE_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDDESTINATION_FIELD_NUMBER: _ClassVar[int]
    CANCELABLE_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    ARRIVALMARKETABILITY_FIELD_NUMBER: _ClassVar[int]
    orderId: int
    symbol: str
    side: _defs_pb2.Side
    price: float
    quantity: float
    orderType: _defs_pb2.OrderType
    session: _defs_pb2.Session
    duration: _defs_pb2.Duration
    enteredTime: _timestamp_pb2.Timestamp
    status: _defs_pb2.Status
    simExchange: bool
    filledQuantity: float
    clordId: str
    orderVersionNum: int
    origorderId: int
    rootorderId: int
    origclordId: str
    rootclordId: str
    orderStrategyType: _defs_pb2.OrderStrategyType
    specialInstruction: _defs_pb2.SpecialInstruction
    bidpx: float
    askpx: float
    sendersubId: str
    accountNumber: int
    stopPrice: float
    requestedDestination: _defs_pb2.RequestedDestination
    cancelable: bool
    editable: bool
    arrivalMarketability: _defs_pb2.Marketability
    def __init__(
        self,
        orderId: _Optional[int] = ...,
        symbol: _Optional[str] = ...,
        side: _Optional[_Union[_defs_pb2.Side, str]] = ...,
        price: _Optional[float] = ...,
        quantity: _Optional[float] = ...,
        orderType: _Optional[_Union[_defs_pb2.OrderType, str]] = ...,
        session: _Optional[_Union[_defs_pb2.Session, str]] = ...,
        duration: _Optional[_Union[_defs_pb2.Duration, str]] = ...,
        enteredTime: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        status: _Optional[_Union[_defs_pb2.Status, str]] = ...,
        simExchange: _Optional[bool] = ...,
        filledQuantity: _Optional[float] = ...,
        clordId: _Optional[str] = ...,
        orderVersionNum: _Optional[int] = ...,
        origorderId: _Optional[int] = ...,
        rootorderId: _Optional[int] = ...,
        origclordId: _Optional[str] = ...,
        rootclordId: _Optional[str] = ...,
        orderStrategyType: _Optional[_Union[_defs_pb2.OrderStrategyType, str]] = ...,
        specialInstruction: _Optional[_Union[_defs_pb2.SpecialInstruction, str]] = ...,
        bidpx: _Optional[float] = ...,
        askpx: _Optional[float] = ...,
        sendersubId: _Optional[str] = ...,
        accountNumber: _Optional[int] = ...,
        stopPrice: _Optional[float] = ...,
        requestedDestination: _Optional[
            _Union[_defs_pb2.RequestedDestination, str]
        ] = ...,
        cancelable: _Optional[bool] = ...,
        editable: _Optional[bool] = ...,
        arrivalMarketability: _Optional[_Union[_defs_pb2.Marketability, str]] = ...,
    ) -> None: ...
