# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ni/measurementlink/pinmap/v1/pin_map_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2ni/measurementlink/pinmap/v1/pin_map_service.proto\x12\x1cni.measurementlink.pinmap.v1\"\x1c\n\x06PinMap\x12\x12\n\npin_map_id\x18\x01 \x01(\t\"E\n\x1a\x43reatePinMapFromXmlRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\x13\n\x0bpin_map_xml\x18\x02 \x01(\t\"E\n\x1aUpdatePinMapFromXmlRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\x13\n\x0bpin_map_xml\x18\x02 \x01(\t\"&\n\x10GetPinMapRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\"B\n\x10QueryPinsRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\x1a\n\x12instrument_type_id\x18\x02 \x01(\t\"\x94\x01\n\x11QueryPinsResponse\x12\x39\n\x04pins\x18\x01 \x03(\x0b\x32+.ni.measurementlink.pinmap.v1.PinDefinition\x12\x44\n\npin_groups\x18\x02 \x03(\x0b\x32\x30.ni.measurementlink.pinmap.v1.PinGroupDefinition\"<\n\rPinDefinition\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x15\n\ris_system_pin\x18\x02 \x01(\x08\"b\n\x12PinGroupDefinition\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x1f\n\x17pin_or_group_references\x18\x02 \x03(\t\x12\x15\n\rresolved_pins\x18\x03 \x03(\t\"(\n\x12QueryRelaysRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\"\x9e\x01\n\x13QueryRelaysResponse\x12=\n\x06relays\x18\x01 \x03(\x0b\x32-.ni.measurementlink.pinmap.v1.RelayDefinition\x12H\n\x0crelay_groups\x18\x02 \x03(\x0b\x32\x32.ni.measurementlink.pinmap.v1.RelayGroupDefinition\"@\n\x0fRelayDefinition\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x17\n\x0fis_system_relay\x18\x02 \x01(\x08\"h\n\x14RelayGroupDefinition\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12!\n\x19relay_or_group_references\x18\x02 \x03(\t\x12\x17\n\x0fresolved_relays\x18\x03 \x03(\t\"\x82\x01\n%QueryResourceAccessInformationRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\r\n\x05sites\x18\x02 \x03(\x05\x12\x1a\n\x12pin_or_relay_names\x18\x03 \x03(\t\x12\x1a\n\x12instrument_type_id\x18\x04 \x01(\t\"\xe1\x02\n&QueryResourceAccessInformationResponse\x12\\\n\x1bresource_access_information\x18\x01 \x03(\x0b\x32\x37.ni.measurementlink.pinmap.v1.ResourceAccessInformation\x12o\n\x0egroup_mappings\x18\x02 \x03(\x0b\x32W.ni.measurementlink.pinmap.v1.QueryResourceAccessInformationResponse.GroupMappingsEntry\x1ah\n\x12GroupMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.ni.measurementlink.pinmap.v1.ResolvedPinsOrRelays:\x02\x38\x01\"\xac\x01\n\x19ResourceAccessInformation\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x1a\n\x12instrument_type_id\x18\x03 \x01(\t\x12\x46\n\x10\x63hannel_mappings\x18\x04 \x03(\x0b\x32,.ni.measurementlink.pinmap.v1.ChannelMapping\"\xa5\x01\n\x0e\x43hannelMapping\x12\x19\n\x11pin_or_relay_name\x18\x01 \x01(\t\x12\x0c\n\x04site\x18\x02 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\t\x12!\n\x19multiplexer_resource_name\x18\x04 \x01(\t\x12\x19\n\x11multiplexer_route\x18\x05 \x01(\t\x12\x1b\n\x13multiplexer_type_id\x18\x06 \x01(\t\"2\n\x14ResolvedPinsOrRelays\x12\x1a\n\x12pin_or_relay_names\x18\x01 \x03(\t2\xf0\x05\n\rPinMapService\x12u\n\x13\x43reatePinMapFromXml\x12\x38.ni.measurementlink.pinmap.v1.CreatePinMapFromXmlRequest\x1a$.ni.measurementlink.pinmap.v1.PinMap\x12u\n\x13UpdatePinMapFromXml\x12\x38.ni.measurementlink.pinmap.v1.UpdatePinMapFromXmlRequest\x1a$.ni.measurementlink.pinmap.v1.PinMap\x12\x61\n\tGetPinMap\x12..ni.measurementlink.pinmap.v1.GetPinMapRequest\x1a$.ni.measurementlink.pinmap.v1.PinMap\x12l\n\tQueryPins\x12..ni.measurementlink.pinmap.v1.QueryPinsRequest\x1a/.ni.measurementlink.pinmap.v1.QueryPinsResponse\x12r\n\x0bQueryRelays\x12\x30.ni.measurementlink.pinmap.v1.QueryRelaysRequest\x1a\x31.ni.measurementlink.pinmap.v1.QueryRelaysResponse\x12\xab\x01\n\x1eQueryResourceAccessInformation\x12\x43.ni.measurementlink.pinmap.v1.QueryResourceAccessInformationRequest\x1a\x44.ni.measurementlink.pinmap.v1.QueryResourceAccessInformationResponseB\xba\x01\n com.ni.measurementlink.pinmap.v1B\x12PinMapServiceProtoP\x01Z\x08pinmapv1\xa2\x02\x04NIMP\xaa\x02-NationalInstruments.MeasurementLink.PinMap.V1\xca\x02\x1cNI\\MeasurementLink\\PinMap\\V1\xea\x02\x1fNI::MeasurementLink::PinMap::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ni.measurementlink.pinmap.v1.pin_map_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.ni.measurementlink.pinmap.v1B\022PinMapServiceProtoP\001Z\010pinmapv1\242\002\004NIMP\252\002-NationalInstruments.MeasurementLink.PinMap.V1\312\002\034NI\\MeasurementLink\\PinMap\\V1\352\002\037NI::MeasurementLink::PinMap::V1'
  _QUERYRESOURCEACCESSINFORMATIONRESPONSE_GROUPMAPPINGSENTRY._options = None
  _QUERYRESOURCEACCESSINFORMATIONRESPONSE_GROUPMAPPINGSENTRY._serialized_options = b'8\001'
  _PINMAP._serialized_start=84
  _PINMAP._serialized_end=112
  _CREATEPINMAPFROMXMLREQUEST._serialized_start=114
  _CREATEPINMAPFROMXMLREQUEST._serialized_end=183
  _UPDATEPINMAPFROMXMLREQUEST._serialized_start=185
  _UPDATEPINMAPFROMXMLREQUEST._serialized_end=254
  _GETPINMAPREQUEST._serialized_start=256
  _GETPINMAPREQUEST._serialized_end=294
  _QUERYPINSREQUEST._serialized_start=296
  _QUERYPINSREQUEST._serialized_end=362
  _QUERYPINSRESPONSE._serialized_start=365
  _QUERYPINSRESPONSE._serialized_end=513
  _PINDEFINITION._serialized_start=515
  _PINDEFINITION._serialized_end=575
  _PINGROUPDEFINITION._serialized_start=577
  _PINGROUPDEFINITION._serialized_end=675
  _QUERYRELAYSREQUEST._serialized_start=677
  _QUERYRELAYSREQUEST._serialized_end=717
  _QUERYRELAYSRESPONSE._serialized_start=720
  _QUERYRELAYSRESPONSE._serialized_end=878
  _RELAYDEFINITION._serialized_start=880
  _RELAYDEFINITION._serialized_end=944
  _RELAYGROUPDEFINITION._serialized_start=946
  _RELAYGROUPDEFINITION._serialized_end=1050
  _QUERYRESOURCEACCESSINFORMATIONREQUEST._serialized_start=1053
  _QUERYRESOURCEACCESSINFORMATIONREQUEST._serialized_end=1183
  _QUERYRESOURCEACCESSINFORMATIONRESPONSE._serialized_start=1186
  _QUERYRESOURCEACCESSINFORMATIONRESPONSE._serialized_end=1539
  _QUERYRESOURCEACCESSINFORMATIONRESPONSE_GROUPMAPPINGSENTRY._serialized_start=1435
  _QUERYRESOURCEACCESSINFORMATIONRESPONSE_GROUPMAPPINGSENTRY._serialized_end=1539
  _RESOURCEACCESSINFORMATION._serialized_start=1542
  _RESOURCEACCESSINFORMATION._serialized_end=1714
  _CHANNELMAPPING._serialized_start=1717
  _CHANNELMAPPING._serialized_end=1882
  _RESOLVEDPINSORRELAYS._serialized_start=1884
  _RESOLVEDPINSORRELAYS._serialized_end=1934
  _PINMAPSERVICE._serialized_start=1937
  _PINMAPSERVICE._serialized_end=2689
# @@protoc_insertion_point(module_scope)
