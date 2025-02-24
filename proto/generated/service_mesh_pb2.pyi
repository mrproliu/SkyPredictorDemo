from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectPoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    client: _ClassVar[DetectPoint]
    server: _ClassVar[DetectPoint]
    proxy: _ClassVar[DetectPoint]

class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP: _ClassVar[Protocol]
    gRPC: _ClassVar[Protocol]
client: DetectPoint
server: DetectPoint
proxy: DetectPoint
HTTP: Protocol
gRPC: Protocol

class KeyStringValuePair(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ServiceMeshMetrics(_message.Message):
    __slots__ = ("httpMetrics", "tcpMetrics")
    HTTPMETRICS_FIELD_NUMBER: _ClassVar[int]
    TCPMETRICS_FIELD_NUMBER: _ClassVar[int]
    httpMetrics: HTTPServiceMeshMetrics
    tcpMetrics: TCPServiceMeshMetrics
    def __init__(self, httpMetrics: _Optional[_Union[HTTPServiceMeshMetrics, _Mapping]] = ..., tcpMetrics: _Optional[_Union[TCPServiceMeshMetrics, _Mapping]] = ...) -> None: ...

class HTTPServiceMeshMetric(_message.Message):
    __slots__ = ("startTime", "endTime", "sourceServiceName", "sourceServiceInstance", "destServiceName", "destServiceInstance", "endpoint", "latency", "responseCode", "status", "protocol", "detectPoint", "tlsMode", "internalErrorCode", "internalRequestLatencyNanos", "internalResponseLatencyNanos", "sourceInstanceProperties", "destInstanceProperties")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCESERVICENAME_FIELD_NUMBER: _ClassVar[int]
    SOURCESERVICEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    DESTSERVICENAME_FIELD_NUMBER: _ClassVar[int]
    DESTSERVICEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    DETECTPOINT_FIELD_NUMBER: _ClassVar[int]
    TLSMODE_FIELD_NUMBER: _ClassVar[int]
    INTERNALERRORCODE_FIELD_NUMBER: _ClassVar[int]
    INTERNALREQUESTLATENCYNANOS_FIELD_NUMBER: _ClassVar[int]
    INTERNALRESPONSELATENCYNANOS_FIELD_NUMBER: _ClassVar[int]
    SOURCEINSTANCEPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DESTINSTANCEPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    startTime: int
    endTime: int
    sourceServiceName: str
    sourceServiceInstance: str
    destServiceName: str
    destServiceInstance: str
    endpoint: str
    latency: int
    responseCode: int
    status: bool
    protocol: Protocol
    detectPoint: DetectPoint
    tlsMode: str
    internalErrorCode: str
    internalRequestLatencyNanos: int
    internalResponseLatencyNanos: int
    sourceInstanceProperties: _containers.RepeatedCompositeFieldContainer[KeyStringValuePair]
    destInstanceProperties: _containers.RepeatedCompositeFieldContainer[KeyStringValuePair]
    def __init__(self, startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., sourceServiceName: _Optional[str] = ..., sourceServiceInstance: _Optional[str] = ..., destServiceName: _Optional[str] = ..., destServiceInstance: _Optional[str] = ..., endpoint: _Optional[str] = ..., latency: _Optional[int] = ..., responseCode: _Optional[int] = ..., status: bool = ..., protocol: _Optional[_Union[Protocol, str]] = ..., detectPoint: _Optional[_Union[DetectPoint, str]] = ..., tlsMode: _Optional[str] = ..., internalErrorCode: _Optional[str] = ..., internalRequestLatencyNanos: _Optional[int] = ..., internalResponseLatencyNanos: _Optional[int] = ..., sourceInstanceProperties: _Optional[_Iterable[_Union[KeyStringValuePair, _Mapping]]] = ..., destInstanceProperties: _Optional[_Iterable[_Union[KeyStringValuePair, _Mapping]]] = ...) -> None: ...

class HTTPServiceMeshMetrics(_message.Message):
    __slots__ = ("metrics",)
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[HTTPServiceMeshMetric]
    def __init__(self, metrics: _Optional[_Iterable[_Union[HTTPServiceMeshMetric, _Mapping]]] = ...) -> None: ...

class TCPServiceMeshMetric(_message.Message):
    __slots__ = ("startTime", "endTime", "sourceServiceName", "sourceServiceInstance", "destServiceName", "destServiceInstance", "detectPoint", "tlsMode", "internalErrorCode", "internalRequestLatencyNanos", "internalResponseLatencyNanos", "sourceInstanceProperties", "destInstanceProperties", "receivedBytes", "sentBytes")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCESERVICENAME_FIELD_NUMBER: _ClassVar[int]
    SOURCESERVICEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    DESTSERVICENAME_FIELD_NUMBER: _ClassVar[int]
    DESTSERVICEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    DETECTPOINT_FIELD_NUMBER: _ClassVar[int]
    TLSMODE_FIELD_NUMBER: _ClassVar[int]
    INTERNALERRORCODE_FIELD_NUMBER: _ClassVar[int]
    INTERNALREQUESTLATENCYNANOS_FIELD_NUMBER: _ClassVar[int]
    INTERNALRESPONSELATENCYNANOS_FIELD_NUMBER: _ClassVar[int]
    SOURCEINSTANCEPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DESTINSTANCEPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RECEIVEDBYTES_FIELD_NUMBER: _ClassVar[int]
    SENTBYTES_FIELD_NUMBER: _ClassVar[int]
    startTime: int
    endTime: int
    sourceServiceName: str
    sourceServiceInstance: str
    destServiceName: str
    destServiceInstance: str
    detectPoint: DetectPoint
    tlsMode: str
    internalErrorCode: str
    internalRequestLatencyNanos: int
    internalResponseLatencyNanos: int
    sourceInstanceProperties: _containers.RepeatedCompositeFieldContainer[KeyStringValuePair]
    destInstanceProperties: _containers.RepeatedCompositeFieldContainer[KeyStringValuePair]
    receivedBytes: int
    sentBytes: int
    def __init__(self, startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., sourceServiceName: _Optional[str] = ..., sourceServiceInstance: _Optional[str] = ..., destServiceName: _Optional[str] = ..., destServiceInstance: _Optional[str] = ..., detectPoint: _Optional[_Union[DetectPoint, str]] = ..., tlsMode: _Optional[str] = ..., internalErrorCode: _Optional[str] = ..., internalRequestLatencyNanos: _Optional[int] = ..., internalResponseLatencyNanos: _Optional[int] = ..., sourceInstanceProperties: _Optional[_Iterable[_Union[KeyStringValuePair, _Mapping]]] = ..., destInstanceProperties: _Optional[_Iterable[_Union[KeyStringValuePair, _Mapping]]] = ..., receivedBytes: _Optional[int] = ..., sentBytes: _Optional[int] = ...) -> None: ...

class TCPServiceMeshMetrics(_message.Message):
    __slots__ = ("metrics",)
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[TCPServiceMeshMetric]
    def __init__(self, metrics: _Optional[_Iterable[_Union[TCPServiceMeshMetric, _Mapping]]] = ...) -> None: ...

class MeshProbeDownstream(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
