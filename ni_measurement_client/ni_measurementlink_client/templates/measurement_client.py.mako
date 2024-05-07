<%page args="measure_docstring, configuration_metadata, output_metadata, service_class, measure_parameters_with_type, measure_parameters, enum_by_class_name, measure_return_values_with_type"/>\
\
"""Python measurement client."""

% if enum_by_class_name:
from enum import Enum
% endif
from functools import cached_property
from typing import Any, Dict, List, NamedTuple, Tuple

import grpc
from google.protobuf import any_pb2

from ni_measurementlink_service._internal.parameter.metadata import ParameterMetadata
from ni_measurementlink_service._internal.parameter.serializer import (
    deserialize_parameters,
    serialize_parameters,
)
from ni_measurementlink_service._internal.stubs.ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni_measurementlink_service._internal.stubs.ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni_measurementlink_service.discovery import DiscoveryClient
from ni_measurementlink_service.pin_map import PinMapClient

_SITES = [0]
_V2_MEASUREMENT_SERVICE_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"
_pin_map_path = ""

class _MeasurementClient:

    def __init__(self, service_class: str):
        self._service_class = service_class
        self._discovery_client = DiscoveryClient()
        self._configuration_metadata_by_id = ${configuration_metadata}
        self._output_metadata_by_id = ${output_metadata}

    @cached_property
    def _measurement_service_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub:
        resolved_service = self._discovery_client.resolve_service(
            _V2_MEASUREMENT_SERVICE_INTERFACE, self._service_class
        )
        channel = grpc.insecure_channel(resolved_service.insecure_address)
        return v2_measurement_service_pb2_grpc.MeasurementServiceStub(channel)


    def _get_measure_request(self, args: Any) -> v2_measurement_service_pb2.MeasureRequest:
        serialized_configuration = any_pb2.Any(
            value=serialize_parameters(self._configuration_metadata_by_id, list(args))
        )
        return v2_measurement_service_pb2.MeasureRequest(
            configuration_parameters=serialized_configuration,
            pin_map_context=PinMapContext(
                pin_map_id=_pin_map_path,
                sites=_SITES,
            ),
        )

    % if enum_by_class_name:

    def _get_enum_type(self, value: Any, is_array: bool) -> type:
        if is_array and len(value) > 0:
            if isinstance(value[0], str):
                return type(eval(value[0]))
            return type(value[0])
        elif isinstance(value, str):
            return type(eval(value))
        else:
            return type(value)


    def _parse_enum_values(
        self, output_values: Dict[int, Any]
    ) -> Dict[int, Any]:
        for key, metadata in self._output_metadata_by_id.items():
            if metadata.annotations and metadata.annotations["ni/type_specialization"] == "enum":
                enum_type = self._get_enum_type(metadata.default_value, metadata.repeated)
                output_values[key] = enum_type(int(output_values[key]))

        return output_values

    % endif

    def _measure(self, *args: Any) -> Tuple[Any]:
        request = self._get_measure_request(args)
        result = [None] * max(self._output_metadata_by_id.keys())
        for response in self._measurement_service_stub.Measure(request):
            output_values = deserialize_parameters(
                self._output_metadata_by_id, response.outputs.value
            )
            % if enum_by_class_name:
            output_values = self._parse_enum_values(output_values)
            % endif
            for k, v in output_values.items():
                result[k - 1] = v

        return tuple(result)

% for enum_name, enum_value in enum_by_class_name.items():

class ${enum_name}(Enum):

    % for key, val in enum_value.items():
    ${key} = ${val}
    % endfor

% endfor

class Output(NamedTuple):
    """Measurement result container."""

    ${measure_return_values_with_type}


def measure(
    ${measure_parameters_with_type}
) -> Output:
    """${measure_docstring}

    Returns:
        Measurement output.
    """

    client = _MeasurementClient("${service_class}")
    response = client._measure(
        ${measure_parameters}
    )
    return Output._make(response)


def register_pin_map(pin_map_absolute_path: str) -> str:
    """Registers the pin map with the pin map service.

    Args:
        pin_map_absolute_path: Absolute path of the pin map.

    Returns:
        Pin map id.
    """

    pin_map_client = PinMapClient()
    global _pin_map_path
    _pin_map_path = pin_map_absolute_path

    return pin_map_client.update_pin_map(_pin_map_path)
