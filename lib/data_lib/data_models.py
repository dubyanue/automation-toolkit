from datetime import datetime

from pydantic import BaseModel, NonNegativeFloat, NonNegativeInt, StrictBool

from data.proto import defs_pb2


class Asset(BaseModel):
    symbol: str
    cusip: str
    description: str
    exchange: str
    assetType: str | None = None
    high52: float | None = None
    low52: float | None = None
    dividendAmount: float | None = 0.0
    dividendYield: float | None = 0.0
    dividendDate: datetime | None = None
    peRatio: float | None = 0.0
    pegRatio: float | None = 200
    pbRatio: float | None = 200
    prRatio: float | None = 200
    pcfRatio: float | None = 0.0
    grossMarginTTM: float | None = 0.0
    grossMarginMRQ: float | None = 0.0
    netProfitMarginTTM: float | None = 0.0
    netProfitMarginMRQ: float | None = 0.0
    operatingMarginTTM: float | None = 0.0
    operatingMarginMRQ: float | None = 0.0
    returnOnEquity: float | None = 0.0
    returnOnAssets: float | None = 0.0
    returnOnInvestment: float | None = 0.0
    quickRatio: float | None = 0.0
    currentRatio: float | None = 0.0
    interestCoverage: float | None = 0.0
    totalDebtToCapital: float | None = 0.0
    ltDebtToEquity: float | None = 0.0
    totalDebtToEquity: float | None = 0.0
    epsTTM: float | None = 0.0
    epsChangePercentTTM: float | None = 0.0
    epsChangeYear: float | None = 0.0
    epsChange: float | None = 0.0
    revChangeYear: float | None = 0.0
    revChangeTTM: float | None = 0.0
    revChangeIn: float | None = 0.0
    sharesOutstanding: float | None = 0.0
    marketCapFloat: float | None = 0.0
    marketCap: float | None = 0.0
    bookValuePerShare: float | None = 0.0
    shortIntToFloat: float | None = 0.0
    shortIntDayToCover: float | None = 0.0
    divGrowthRate3Year: float | None = 0.0
    dividendPayAmount: float | None = 0.0
    dividendPayDate: datetime | None = None
    beta: float | None = 0.0
    avg10DaysVolume: NonNegativeInt | None = 0
    avg1DayVolume: NonNegativeInt | None = 0
    avg3MonthVolume: NonNegativeInt | None = 0
    declarationDate: datetime | None = None
    dividendFreq: int | None = None
    eps: float | None = 0.0
    dtnVolume: int | None = None
    nextDividendPayDate: datetime | None = None
    nextDividendDate: datetime | None = None
    divPayAmount: float | None = 0.0
    divFreq: NonNegativeInt | None = 0
    avg1YearVolume: NonNegativeInt | None = 0
    divYield: float | None = 0.0
    nextDivPayDate: datetime | None = None
    nextDivExDate: datetime | None = None
    divPayDate: datetime | None = None
    lastEarningsDate: datetime | None = None
    divAmount: float | None = 0.0
    divExDate: datetime | None = None
    assetMainType: str | None = None
    downloadDate: datetime | None = None
    openPrice: float | None = 0.0
    closePrice: float | None = 0.0
    exchangeName: str
    securityStatus: str | None = None
    ssid: int


class Order(BaseModel):
    orderId: int
    symbol: str
    side: str
    price: NonNegativeFloat | None = None
    quantity: NonNegativeFloat
    orderType: str
    session: str | None = None
    duration: str
    enteredTime: datetime | None = None
    status: str | None = None
    simExchange: StrictBool = False
    filledQuantity: NonNegativeFloat | None = 0.0
    remainingQuantity: NonNegativeFloat | None = 0.0
    clordId: str
    clientId: str
    orderVersionNum: NonNegativeInt | None = 0
    origorderId: int
    rootorderId: int
    origclordId: str
    rootclordId: str
    orderStrategyType: str | None = defs_pb2.OrderStrategyType.Name(defs_pb2.SINGLE)
    specialInstruction: str | None = defs_pb2.SpecialInstruction.Name(
        defs_pb2.NO_SPECIAL_INSTRUCTION
    )
    bidpx: NonNegativeFloat | None = 0.0
    askpx: NonNegativeFloat | None = 0.0
    sendersubId: str | None = None
    accountNumber: int | None = None
    stopPrice: NonNegativeFloat | None = 0.0
    requestedDestination: str | None = defs_pb2.RequestedDestination.Name(
        defs_pb2.NO_REQUESTED_DESTINATION
    )
    cancelable: StrictBool = False
    editable: StrictBool = False
    arrivalMarketability: str | None = defs_pb2.Marketability.Name(
        defs_pb2.NON_MARKETABLE
    )
