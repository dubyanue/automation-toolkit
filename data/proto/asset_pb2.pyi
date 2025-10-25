import datetime
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ()
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSETTYPE_FIELD_NUMBER: _ClassVar[int]
    HIGH52_FIELD_NUMBER: _ClassVar[int]
    LOW52_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDYIELD_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDDATE_FIELD_NUMBER: _ClassVar[int]
    PERATIO_FIELD_NUMBER: _ClassVar[int]
    PEGRATIO_FIELD_NUMBER: _ClassVar[int]
    PBRATIO_FIELD_NUMBER: _ClassVar[int]
    PRRATIO_FIELD_NUMBER: _ClassVar[int]
    PCFRATIO_FIELD_NUMBER: _ClassVar[int]
    GROSSMARGINTTM_FIELD_NUMBER: _ClassVar[int]
    GROSSMARGINMRQ_FIELD_NUMBER: _ClassVar[int]
    NETPROFITMARGINTTM_FIELD_NUMBER: _ClassVar[int]
    NETPROFITMARGINMRQ_FIELD_NUMBER: _ClassVar[int]
    OPERATINGMARGINTTM_FIELD_NUMBER: _ClassVar[int]
    OPERATINGMARGINMRQ_FIELD_NUMBER: _ClassVar[int]
    RETURNONEQUITY_FIELD_NUMBER: _ClassVar[int]
    RETURNONASSETS_FIELD_NUMBER: _ClassVar[int]
    RETURNONINVESTMENT_FIELD_NUMBER: _ClassVar[int]
    QUICKRATIO_FIELD_NUMBER: _ClassVar[int]
    CURRENTRATIO_FIELD_NUMBER: _ClassVar[int]
    INTERESTCOVERAGE_FIELD_NUMBER: _ClassVar[int]
    TOTALDEBTTOCAPITAL_FIELD_NUMBER: _ClassVar[int]
    LTDEBTTOEQUITY_FIELD_NUMBER: _ClassVar[int]
    TOTALDEBTTOEQUITY_FIELD_NUMBER: _ClassVar[int]
    EPSTTM_FIELD_NUMBER: _ClassVar[int]
    EPSCHANGEPERCENTTTM_FIELD_NUMBER: _ClassVar[int]
    EPSCHANGEYEAR_FIELD_NUMBER: _ClassVar[int]
    EPSCHANGE_FIELD_NUMBER: _ClassVar[int]
    REVCHANGEYEAR_FIELD_NUMBER: _ClassVar[int]
    REVCHANGETTM_FIELD_NUMBER: _ClassVar[int]
    REVCHANGEIN_FIELD_NUMBER: _ClassVar[int]
    SHARESOUTSTANDING_FIELD_NUMBER: _ClassVar[int]
    MARKETCAPFLOAT_FIELD_NUMBER: _ClassVar[int]
    MARKETCAP_FIELD_NUMBER: _ClassVar[int]
    BOOKVALUEPERSHARE_FIELD_NUMBER: _ClassVar[int]
    SHORTINTTOFLOAT_FIELD_NUMBER: _ClassVar[int]
    SHORTINTDAYTOCOVER_FIELD_NUMBER: _ClassVar[int]
    DIVGROWTHRATE3YEAR_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDPAYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDPAYDATE_FIELD_NUMBER: _ClassVar[int]
    BETA_FIELD_NUMBER: _ClassVar[int]
    AVG10DAYSVOLUME_FIELD_NUMBER: _ClassVar[int]
    AVG1DAYVOLUME_FIELD_NUMBER: _ClassVar[int]
    AVG3MONTHVOLUME_FIELD_NUMBER: _ClassVar[int]
    DECLARATIONDATE_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDFREQ_FIELD_NUMBER: _ClassVar[int]
    EPS_FIELD_NUMBER: _ClassVar[int]
    DTNVOLUME_FIELD_NUMBER: _ClassVar[int]
    NEXTDIVIDENDPAYDATE_FIELD_NUMBER: _ClassVar[int]
    NEXTDIVIDENDDATE_FIELD_NUMBER: _ClassVar[int]
    DIVPAYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    DIVFREQ_FIELD_NUMBER: _ClassVar[int]
    AVG1YEARVOLUME_FIELD_NUMBER: _ClassVar[int]
    DIVYIELD_FIELD_NUMBER: _ClassVar[int]
    NEXTDIVPAYDATE_FIELD_NUMBER: _ClassVar[int]
    NEXTDIVEXDATE_FIELD_NUMBER: _ClassVar[int]
    DIVPAYDATE_FIELD_NUMBER: _ClassVar[int]
    LASTEARNINGSDATE_FIELD_NUMBER: _ClassVar[int]
    DIVAMOUNT_FIELD_NUMBER: _ClassVar[int]
    DIVEXDATE_FIELD_NUMBER: _ClassVar[int]
    ASSETMAINTYPE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADDATE_FIELD_NUMBER: _ClassVar[int]
    CLOSEPRICE_FIELD_NUMBER: _ClassVar[int]
    OPENPRICE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGENAME_FIELD_NUMBER: _ClassVar[int]
    SECURITYSTATUS_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    cusip: str
    description: str
    exchange: str
    assetType: str
    high52: float
    low52: float
    dividendAmount: float
    dividendYield: float
    dividendDate: _timestamp_pb2.Timestamp
    peRatio: float
    pegRatio: float
    pbRatio: float
    prRatio: float
    pcfRatio: float
    grossMarginTTM: float
    grossMarginMRQ: float
    netProfitMarginTTM: float
    netProfitMarginMRQ: float
    operatingMarginTTM: float
    operatingMarginMRQ: float
    returnOnEquity: float
    returnOnAssets: float
    returnOnInvestment: float
    quickRatio: float
    currentRatio: float
    interestCoverage: float
    totalDebtToCapital: float
    ltDebtToEquity: float
    totalDebtToEquity: float
    epsTTM: float
    epsChangePercentTTM: float
    epsChangeYear: float
    epsChange: float
    revChangeYear: float
    revChangeTTM: float
    revChangeIn: float
    sharesOutstanding: float
    marketCapFloat: float
    marketCap: float
    bookValuePerShare: float
    shortIntToFloat: float
    shortIntDayToCover: float
    divGrowthRate3Year: float
    dividendPayAmount: float
    dividendPayDate: _timestamp_pb2.Timestamp
    beta: float
    avg10DaysVolume: float
    avg1DayVolume: float
    avg3MonthVolume: float
    declarationDate: _timestamp_pb2.Timestamp
    dividendFreq: int
    eps: float
    dtnVolume: int
    nextDividendPayDate: _timestamp_pb2.Timestamp
    nextDividendDate: _timestamp_pb2.Timestamp
    divPayAmount: float
    divFreq: int
    avg1YearVolume: float
    divYield: float
    nextDivPayDate: _timestamp_pb2.Timestamp
    nextDivExDate: _timestamp_pb2.Timestamp
    divPayDate: _timestamp_pb2.Timestamp
    lastEarningsDate: _timestamp_pb2.Timestamp
    divAmount: float
    divExDate: _timestamp_pb2.Timestamp
    assetMainType: str
    downloadDate: _timestamp_pb2.Timestamp
    closePrice: float
    openPrice: float
    exchangeName: str
    securityStatus: str
    ssid: int
    def __init__(
        self,
        symbol: _Optional[str] = ...,
        cusip: _Optional[str] = ...,
        description: _Optional[str] = ...,
        exchange: _Optional[str] = ...,
        assetType: _Optional[str] = ...,
        high52: _Optional[float] = ...,
        low52: _Optional[float] = ...,
        dividendAmount: _Optional[float] = ...,
        dividendYield: _Optional[float] = ...,
        dividendDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        peRatio: _Optional[float] = ...,
        pegRatio: _Optional[float] = ...,
        pbRatio: _Optional[float] = ...,
        prRatio: _Optional[float] = ...,
        pcfRatio: _Optional[float] = ...,
        grossMarginTTM: _Optional[float] = ...,
        grossMarginMRQ: _Optional[float] = ...,
        netProfitMarginTTM: _Optional[float] = ...,
        netProfitMarginMRQ: _Optional[float] = ...,
        operatingMarginTTM: _Optional[float] = ...,
        operatingMarginMRQ: _Optional[float] = ...,
        returnOnEquity: _Optional[float] = ...,
        returnOnAssets: _Optional[float] = ...,
        returnOnInvestment: _Optional[float] = ...,
        quickRatio: _Optional[float] = ...,
        currentRatio: _Optional[float] = ...,
        interestCoverage: _Optional[float] = ...,
        totalDebtToCapital: _Optional[float] = ...,
        ltDebtToEquity: _Optional[float] = ...,
        totalDebtToEquity: _Optional[float] = ...,
        epsTTM: _Optional[float] = ...,
        epsChangePercentTTM: _Optional[float] = ...,
        epsChangeYear: _Optional[float] = ...,
        epsChange: _Optional[float] = ...,
        revChangeYear: _Optional[float] = ...,
        revChangeTTM: _Optional[float] = ...,
        revChangeIn: _Optional[float] = ...,
        sharesOutstanding: _Optional[float] = ...,
        marketCapFloat: _Optional[float] = ...,
        marketCap: _Optional[float] = ...,
        bookValuePerShare: _Optional[float] = ...,
        shortIntToFloat: _Optional[float] = ...,
        shortIntDayToCover: _Optional[float] = ...,
        divGrowthRate3Year: _Optional[float] = ...,
        dividendPayAmount: _Optional[float] = ...,
        dividendPayDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        beta: _Optional[float] = ...,
        avg10DaysVolume: _Optional[float] = ...,
        avg1DayVolume: _Optional[float] = ...,
        avg3MonthVolume: _Optional[float] = ...,
        declarationDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        dividendFreq: _Optional[int] = ...,
        eps: _Optional[float] = ...,
        dtnVolume: _Optional[int] = ...,
        nextDividendPayDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        nextDividendDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        divPayAmount: _Optional[float] = ...,
        divFreq: _Optional[int] = ...,
        avg1YearVolume: _Optional[float] = ...,
        divYield: _Optional[float] = ...,
        nextDivPayDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        nextDivExDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        divPayDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        lastEarningsDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        divAmount: _Optional[float] = ...,
        divExDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        assetMainType: _Optional[str] = ...,
        downloadDate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        closePrice: _Optional[float] = ...,
        openPrice: _Optional[float] = ...,
        exchangeName: _Optional[str] = ...,
        securityStatus: _Optional[str] = ...,
        ssid: _Optional[int] = ...,
    ) -> None: ...
