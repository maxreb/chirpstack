# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/gw/gw.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hirpstack-api/gw/gw.proto\x12\x02gw\x1a\"chirpstack-api/common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x95\x01\n\nModulation\x12&\n\x04lora\x18\x03 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12$\n\x03\x66sk\x18\x04 \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12+\n\x07lr_fhss\x18\x05 \x01(\x0b\x32\x18.gw.LrFhssModulationInfoH\x00\x42\x0c\n\nparameters\"\x8d\x02\n\x12UplinkTxInfoLegacy\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12&\n\nmodulation\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12\x36\n\x14lora_modulation_info\x18\x03 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12\x34\n\x13\x66sk_modulation_info\x18\x04 \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12;\n\x17lr_fhss_modulation_info\x18\x05 \x01(\x0b\x32\x18.gw.LrFhssModulationInfoH\x00\x42\x11\n\x0fmodulation_info\"E\n\x0cUplinkTxInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\"\n\nmodulation\x18\x02 \x01(\x0b\x32\x0e.gw.Modulation\"\x9c\x01\n\x12LoraModulationInfo\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x18\n\x10spreading_factor\x18\x02 \x01(\r\x12\x18\n\x10\x63ode_rate_legacy\x18\x03 \x01(\t\x12\x1f\n\tcode_rate\x18\x05 \x01(\x0e\x32\x0c.gw.CodeRate\x12\x1e\n\x16polarization_inversion\x18\x04 \x01(\x08\"B\n\x11\x46skModulationInfo\x12\x1b\n\x13\x66requency_deviation\x18\x01 \x01(\r\x12\x10\n\x08\x64\x61tarate\x18\x02 \x01(\r\"\x86\x01\n\x14LrFhssModulationInfo\x12\x1f\n\x17operating_channel_width\x18\x01 \x01(\r\x12\x18\n\x10\x63ode_rate_legacy\x18\x02 \x01(\t\x12\x1f\n\tcode_rate\x18\x04 \x01(\x0e\x32\x0c.gw.CodeRate\x12\x12\n\ngrid_steps\x18\x03 \x01(\r\"V\n\x16\x45ncryptedFineTimestamp\x12\x15\n\raes_key_index\x18\x01 \x01(\r\x12\x14\n\x0c\x65ncrypted_ns\x18\x02 \x01(\x0c\x12\x0f\n\x07\x66pga_id\x18\x03 \x01(\x0c\">\n\x12PlainFineTimestamp\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x90\x07\n\x0cGatewayStats\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x11 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x08location\x18\x03 \x01(\x0b\x32\x10.common.Location\x12\x16\n\x0e\x63onfig_version\x18\x04 \x01(\t\x12\x1b\n\x13rx_packets_received\x18\x05 \x01(\r\x12\x1e\n\x16rx_packets_received_ok\x18\x06 \x01(\r\x12\x1b\n\x13tx_packets_received\x18\x07 \x01(\r\x12\x1a\n\x12tx_packets_emitted\x18\x08 \x01(\r\x12\x30\n\x08metadata\x18\n \x03(\x0b\x32\x1e.gw.GatewayStats.MetadataEntry\x12M\n\x18tx_packets_per_frequency\x18\x0c \x03(\x0b\x32+.gw.GatewayStats.TxPacketsPerFrequencyEntry\x12M\n\x18rx_packets_per_frequency\x18\r \x03(\x0b\x32+.gw.GatewayStats.RxPacketsPerFrequencyEntry\x12\x39\n\x19tx_packets_per_modulation\x18\x0e \x03(\x0b\x32\x16.gw.PerModulationCount\x12\x39\n\x19rx_packets_per_modulation\x18\x0f \x03(\x0b\x32\x16.gw.PerModulationCount\x12G\n\x15tx_packets_per_status\x18\x10 \x03(\x0b\x32(.gw.GatewayStats.TxPacketsPerStatusEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"G\n\x12PerModulationCount\x12\"\n\nmodulation\x18\x01 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\x80\x05\n\x12UplinkRxInfoLegacy\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_since_gps_epoch\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x10\n\x08lora_snr\x18\x06 \x01(\x01\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\x12\x10\n\x08rf_chain\x18\x08 \x01(\r\x12\r\n\x05\x62oard\x18\t \x01(\r\x12\x0f\n\x07\x61ntenna\x18\n \x01(\r\x12\"\n\x08location\x18\x0b \x01(\x0b\x32\x10.common.Location\x12\x32\n\x13\x66ine_timestamp_type\x18\x0c \x01(\x0e\x32\x15.gw.FineTimestampType\x12>\n\x18\x65ncrypted_fine_timestamp\x18\r \x01(\x0b\x32\x1a.gw.EncryptedFineTimestampH\x00\x12\x36\n\x14plain_fine_timestamp\x18\x0e \x01(\x0b\x32\x16.gw.PlainFineTimestampH\x00\x12\x0f\n\x07\x63ontext\x18\x0f \x01(\x0c\x12\x11\n\tuplink_id\x18\x10 \x01(\x0c\x12!\n\ncrc_status\x18\x11 \x01(\x0e\x32\r.gw.CRCStatus\x12\x36\n\x08metadata\x18\x12 \x03(\x0b\x32$.gw.UplinkRxInfoLegacy.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x10\n\x0e\x66ine_timestamp\"\xef\x03\n\x0cUplinkRxInfo\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12\x11\n\tuplink_id\x18\x02 \x01(\r\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_since_gps_epoch\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x19\x66ine_time_since_gps_epoch\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04rssi\x18\x06 \x01(\x05\x12\x0b\n\x03snr\x18\x07 \x01(\x02\x12\x0f\n\x07\x63hannel\x18\x08 \x01(\r\x12\x10\n\x08rf_chain\x18\t \x01(\r\x12\r\n\x05\x62oard\x18\n \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x0b \x01(\r\x12\"\n\x08location\x18\x0c \x01(\x0b\x32\x10.common.Location\x12\x0f\n\x07\x63ontext\x18\r \x01(\x0c\x12\x30\n\x08metadata\x18\x0f \x03(\x0b\x32\x1e.gw.UplinkRxInfo.MetadataEntry\x12!\n\ncrc_status\x18\x10 \x01(\x0e\x32\r.gw.CRCStatus\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x82\x04\n\x14\x44ownlinkTxInfoLegacy\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x11\n\tfrequency\x18\x05 \x01(\r\x12\r\n\x05power\x18\x06 \x01(\x05\x12&\n\nmodulation\x18\x07 \x01(\x0e\x32\x12.common.Modulation\x12\x36\n\x14lora_modulation_info\x18\x08 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12\x34\n\x13\x66sk_modulation_info\x18\t \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12\r\n\x05\x62oard\x18\n \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x0b \x01(\r\x12\"\n\x06timing\x18\x0c \x01(\x0e\x32\x12.gw.DownlinkTiming\x12<\n\x17immediately_timing_info\x18\r \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x01\x12\x30\n\x11\x64\x65lay_timing_info\x18\x0e \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x01\x12\x37\n\x15gps_epoch_timing_info\x18\x0f \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x01\x12\x0f\n\x07\x63ontext\x18\x10 \x01(\x0c\x42\x11\n\x0fmodulation_infoB\r\n\x0btiming_info\"\xa3\x01\n\x0e\x44ownlinkTxInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\r\n\x05power\x18\x02 \x01(\x05\x12\"\n\nmodulation\x18\x03 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x62oard\x18\x04 \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x05 \x01(\r\x12\x1a\n\x06timing\x18\x06 \x01(\x0b\x32\n.gw.Timing\x12\x0f\n\x07\x63ontext\x18\x07 \x01(\x0c\"\x9b\x01\n\x06Timing\x12\x30\n\x0bimmediately\x18\x01 \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x00\x12$\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x00\x12+\n\tgps_epoch\x18\x03 \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x00\x42\x0c\n\nparameters\"\x17\n\x15ImmediatelyTimingInfo\";\n\x0f\x44\x65layTimingInfo\x12(\n\x05\x64\x65lay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"M\n\x12GPSEpochTimingInfo\x12\x37\n\x14time_since_gps_epoch\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xc8\x01\n\x0bUplinkFrame\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12.\n\x0etx_info_legacy\x18\x02 \x01(\x0b\x32\x16.gw.UplinkTxInfoLegacy\x12.\n\x0erx_info_legacy\x18\x03 \x01(\x0b\x32\x16.gw.UplinkRxInfoLegacy\x12!\n\x07tx_info\x18\x04 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x05 \x01(\x0b\x32\x10.gw.UplinkRxInfo\"k\n\x0eUplinkFrameSet\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRxInfo\"\x95\x01\n\rDownlinkFrame\x12\x13\n\x0b\x64ownlink_id\x18\x03 \x01(\r\x12\x1a\n\x12\x64ownlink_id_legacy\x18\x04 \x01(\x0c\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkFrameItem\x12\x19\n\x11gateway_id_legacy\x18\x06 \x01(\x0c\x12\x12\n\ngateway_id\x18\x07 \x01(\t\"\x7f\n\x11\x44ownlinkFrameItem\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12\x30\n\x0etx_info_legacy\x18\x02 \x01(\x0b\x32\x18.gw.DownlinkTxInfoLegacy\x12#\n\x07tx_info\x18\x03 \x01(\x0b\x32\x12.gw.DownlinkTxInfo\"\x95\x01\n\rDownlinkTxAck\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x13\n\x0b\x64ownlink_id\x18\x02 \x01(\r\x12\x1a\n\x12\x64ownlink_id_legacy\x18\x04 \x01(\x0c\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkTxAckItem\"4\n\x11\x44ownlinkTxAckItem\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.gw.TxAckStatus\"\xb5\x01\n\x14GatewayConfiguration\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12*\n\x08\x63hannels\x18\x03 \x03(\x0b\x32\x18.gw.ChannelConfiguration\x12\x31\n\x0estats_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x87\x02\n\x14\x43hannelConfiguration\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12-\n\x11modulation_legacy\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12:\n\x16lora_modulation_config\x18\x03 \x01(\x0b\x32\x18.gw.LoraModulationConfigH\x00\x12\x38\n\x15\x66sk_modulation_config\x18\x04 \x01(\x0b\x32\x17.gw.FskModulationConfigH\x00\x12\r\n\x05\x62oard\x18\x05 \x01(\r\x12\x13\n\x0b\x64\x65modulator\x18\x06 \x01(\rB\x13\n\x11modulation_config\"^\n\x14LoraModulationConfig\x12\x18\n\x10\x62\x61ndwidth_legacy\x18\x01 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x19\n\x11spreading_factors\x18\x02 \x03(\r\"S\n\x13\x46skModulationConfig\x12\x18\n\x10\x62\x61ndwidth_legacy\x18\x01 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x02 \x01(\r\"\xf4\x01\n\x19GatewayCommandExecRequest\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x0f\n\x07\x65xec_id\x18\x07 \x01(\r\x12\r\n\x05stdin\x18\x04 \x01(\x0c\x12\x43\n\x0b\x65nvironment\x18\x05 \x03(\x0b\x32..gw.GatewayCommandExecRequest.EnvironmentEntry\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8b\x01\n\x1aGatewayCommandExecResponse\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x0f\n\x07\x65xec_id\x18\x07 \x01(\r\x12\x0e\n\x06stdout\x18\x03 \x01(\x0c\x12\x0e\n\x06stderr\x18\x04 \x01(\x0c\x12\r\n\x05\x65rror\x18\x05 \x01(\t\"Y\n\x17RawPacketForwarderEvent\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x04 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"[\n\x19RawPacketForwarderCommand\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x04 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\x80\x01\n\tConnState\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x03 \x01(\t\x12\"\n\x05state\x18\x02 \x01(\x0e\x32\x13.gw.ConnState.State\" \n\x05State\x12\x0b\n\x07OFFLINE\x10\x00\x12\n\n\x06ONLINE\x10\x01*\xb5\x01\n\x08\x43odeRate\x12\x10\n\x0c\x43R_UNDEFINED\x10\x00\x12\n\n\x06\x43R_4_5\x10\x01\x12\n\n\x06\x43R_4_6\x10\x02\x12\n\n\x06\x43R_4_7\x10\x03\x12\n\n\x06\x43R_4_8\x10\x04\x12\n\n\x06\x43R_3_8\x10\x05\x12\n\n\x06\x43R_2_6\x10\x06\x12\n\n\x06\x43R_1_4\x10\x07\x12\n\n\x06\x43R_1_6\x10\x08\x12\n\n\x06\x43R_5_6\x10\t\x12\r\n\tCR_LI_4_5\x10\n\x12\r\n\tCR_LI_4_6\x10\x0b\x12\r\n\tCR_LI_4_8\x10\x0c*;\n\x0e\x44ownlinkTiming\x12\x0f\n\x0bIMMEDIATELY\x10\x00\x12\t\n\x05\x44\x45LAY\x10\x01\x12\r\n\tGPS_EPOCH\x10\x02*7\n\x11\x46ineTimestampType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tENCRYPTED\x10\x01\x12\t\n\x05PLAIN\x10\x02*0\n\tCRCStatus\x12\n\n\x06NO_CRC\x10\x00\x12\x0b\n\x07\x42\x41\x44_CRC\x10\x01\x12\n\n\x06\x43RC_OK\x10\x02*\xbc\x01\n\x0bTxAckStatus\x12\x0b\n\x07IGNORED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0c\n\x08TOO_LATE\x10\x02\x12\r\n\tTOO_EARLY\x10\x03\x12\x14\n\x10\x43OLLISION_PACKET\x10\x04\x12\x14\n\x10\x43OLLISION_BEACON\x10\x05\x12\x0b\n\x07TX_FREQ\x10\x06\x12\x0c\n\x08TX_POWER\x10\x07\x12\x10\n\x0cGPS_UNLOCKED\x10\x08\x12\x0e\n\nQUEUE_FULL\x10\t\x12\x12\n\x0eINTERNAL_ERROR\x10\nBU\n\x14io.chirpstack.api.gwB\x0cGatewayProtoP\x01Z-github.com/chirpstack/chirpstack/api/go/v4/gwb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.gw.gw_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024io.chirpstack.api.gwB\014GatewayProtoP\001Z-github.com/chirpstack/chirpstack/api/go/v4/gw'
  _GATEWAYSTATS_METADATAENTRY._options = None
  _GATEWAYSTATS_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_options = b'8\001'
  _UPLINKRXINFOLEGACY_METADATAENTRY._options = None
  _UPLINKRXINFOLEGACY_METADATAENTRY._serialized_options = b'8\001'
  _UPLINKRXINFO_METADATAENTRY._options = None
  _UPLINKRXINFO_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._options = None
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_options = b'8\001'
  _CODERATE._serialized_start=6446
  _CODERATE._serialized_end=6627
  _DOWNLINKTIMING._serialized_start=6629
  _DOWNLINKTIMING._serialized_end=6688
  _FINETIMESTAMPTYPE._serialized_start=6690
  _FINETIMESTAMPTYPE._serialized_end=6745
  _CRCSTATUS._serialized_start=6747
  _CRCSTATUS._serialized_end=6795
  _TXACKSTATUS._serialized_start=6798
  _TXACKSTATUS._serialized_end=6986
  _MODULATION._serialized_start=166
  _MODULATION._serialized_end=315
  _UPLINKTXINFOLEGACY._serialized_start=318
  _UPLINKTXINFOLEGACY._serialized_end=587
  _UPLINKTXINFO._serialized_start=589
  _UPLINKTXINFO._serialized_end=658
  _LORAMODULATIONINFO._serialized_start=661
  _LORAMODULATIONINFO._serialized_end=817
  _FSKMODULATIONINFO._serialized_start=819
  _FSKMODULATIONINFO._serialized_end=885
  _LRFHSSMODULATIONINFO._serialized_start=888
  _LRFHSSMODULATIONINFO._serialized_end=1022
  _ENCRYPTEDFINETIMESTAMP._serialized_start=1024
  _ENCRYPTEDFINETIMESTAMP._serialized_end=1110
  _PLAINFINETIMESTAMP._serialized_start=1112
  _PLAINFINETIMESTAMP._serialized_end=1174
  _GATEWAYSTATS._serialized_start=1177
  _GATEWAYSTATS._serialized_end=2089
  _GATEWAYSTATS_METADATAENTRY._serialized_start=1859
  _GATEWAYSTATS_METADATAENTRY._serialized_end=1906
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_start=1908
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_end=1968
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_start=1970
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_end=2030
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_start=2032
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_end=2089
  _PERMODULATIONCOUNT._serialized_start=2091
  _PERMODULATIONCOUNT._serialized_end=2162
  _UPLINKRXINFOLEGACY._serialized_start=2165
  _UPLINKRXINFOLEGACY._serialized_end=2805
  _UPLINKRXINFOLEGACY_METADATAENTRY._serialized_start=1859
  _UPLINKRXINFOLEGACY_METADATAENTRY._serialized_end=1906
  _UPLINKRXINFO._serialized_start=2808
  _UPLINKRXINFO._serialized_end=3303
  _UPLINKRXINFO_METADATAENTRY._serialized_start=1859
  _UPLINKRXINFO_METADATAENTRY._serialized_end=1906
  _DOWNLINKTXINFOLEGACY._serialized_start=3306
  _DOWNLINKTXINFOLEGACY._serialized_end=3820
  _DOWNLINKTXINFO._serialized_start=3823
  _DOWNLINKTXINFO._serialized_end=3986
  _TIMING._serialized_start=3989
  _TIMING._serialized_end=4144
  _IMMEDIATELYTIMINGINFO._serialized_start=4146
  _IMMEDIATELYTIMINGINFO._serialized_end=4169
  _DELAYTIMINGINFO._serialized_start=4171
  _DELAYTIMINGINFO._serialized_end=4230
  _GPSEPOCHTIMINGINFO._serialized_start=4232
  _GPSEPOCHTIMINGINFO._serialized_end=4309
  _UPLINKFRAME._serialized_start=4312
  _UPLINKFRAME._serialized_end=4512
  _UPLINKFRAMESET._serialized_start=4514
  _UPLINKFRAMESET._serialized_end=4621
  _DOWNLINKFRAME._serialized_start=4624
  _DOWNLINKFRAME._serialized_end=4773
  _DOWNLINKFRAMEITEM._serialized_start=4775
  _DOWNLINKFRAMEITEM._serialized_end=4902
  _DOWNLINKTXACK._serialized_start=4905
  _DOWNLINKTXACK._serialized_end=5054
  _DOWNLINKTXACKITEM._serialized_start=5056
  _DOWNLINKTXACKITEM._serialized_end=5108
  _GATEWAYCONFIGURATION._serialized_start=5111
  _GATEWAYCONFIGURATION._serialized_end=5292
  _CHANNELCONFIGURATION._serialized_start=5295
  _CHANNELCONFIGURATION._serialized_end=5558
  _LORAMODULATIONCONFIG._serialized_start=5560
  _LORAMODULATIONCONFIG._serialized_end=5654
  _FSKMODULATIONCONFIG._serialized_start=5656
  _FSKMODULATIONCONFIG._serialized_end=5739
  _GATEWAYCOMMANDEXECREQUEST._serialized_start=5742
  _GATEWAYCOMMANDEXECREQUEST._serialized_end=5986
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_start=5936
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_end=5986
  _GATEWAYCOMMANDEXECRESPONSE._serialized_start=5989
  _GATEWAYCOMMANDEXECRESPONSE._serialized_end=6128
  _RAWPACKETFORWARDEREVENT._serialized_start=6130
  _RAWPACKETFORWARDEREVENT._serialized_end=6219
  _RAWPACKETFORWARDERCOMMAND._serialized_start=6221
  _RAWPACKETFORWARDERCOMMAND._serialized_end=6312
  _CONNSTATE._serialized_start=6315
  _CONNSTATE._serialized_end=6443
  _CONNSTATE_STATE._serialized_start=6411
  _CONNSTATE_STATE._serialized_end=6443
# @@protoc_insertion_point(module_scope)
