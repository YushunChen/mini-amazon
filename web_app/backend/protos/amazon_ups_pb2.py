# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/amazon_ups.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/amazon_ups.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17protos/amazon_ups.proto\"\x84\x01\n\tAUCommand\x12(\n\x0epickupRequests\x18\x01 \x03(\x0b\x32\x10.AUPickupRequest\x12*\n\x0f\x64\x65liverRequests\x18\x02 \x03(\x0b\x32\x11.AUDeliverRequest\x12\x0c\n\x04\x61\x63ks\x18\x03 \x03(\x03\x12\x13\n\x05\x65rror\x18\x04 \x03(\x0b\x32\x04.Err\"u\n\tUACommand\x12$\n\x0cloadRequests\x18\x01 \x03(\x0b\x32\x0e.UALoadRequest\x12\x1f\n\tdelivered\x18\x02 \x03(\x0b\x32\x0c.UADelivered\x12\x0c\n\x04\x61\x63ks\x18\x03 \x03(\x03\x12\x13\n\x05\x65rror\x18\x04 \x03(\x0b\x32\x04.Err\"*\n\x07UAstart\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"\x88\x01\n\x0f\x41UPickupRequest\x12\x0e\n\x06seqNum\x18\x01 \x02(\x03\x12\x0e\n\x06shipId\x18\x02 \x02(\x03\x12\x13\n\x0bwarehouseId\x18\x03 \x02(\x03\x12\t\n\x01x\x18\x04 \x02(\x05\x12\t\n\x01y\x18\x05 \x02(\x05\x12\x14\n\x0c\x64\x65stinationX\x18\x06 \x02(\x05\x12\x14\n\x0c\x64\x65stinationY\x18\x07 \x02(\x05\"@\n\rUALoadRequest\x12\x0e\n\x06seqNum\x18\x01 \x02(\x03\x12\x0f\n\x07truckId\x18\x02 \x02(\x05\x12\x0e\n\x06shipId\x18\x03 \x02(\x03\"2\n\x10\x41UDeliverRequest\x12\x0e\n\x06seqNum\x18\x01 \x02(\x03\x12\x0e\n\x06shipId\x18\x02 \x02(\x03\"-\n\x0bUADelivered\x12\x0e\n\x06seqNum\x18\x01 \x02(\x03\x12\x0e\n\x06shipId\x18\x02 \x02(\x03\"8\n\x03\x45rr\x12\x0b\n\x03\x65rr\x18\x01 \x02(\t\x12\x14\n\x0coriginSeqNum\x18\x02 \x02(\x03\x12\x0e\n\x06seqNum\x18\x03 \x02(\x03')
)




_AUCOMMAND = _descriptor.Descriptor(
  name='AUCommand',
  full_name='AUCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pickupRequests', full_name='AUCommand.pickupRequests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deliverRequests', full_name='AUCommand.deliverRequests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acks', full_name='AUCommand.acks', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='AUCommand.error', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=160,
)


_UACOMMAND = _descriptor.Descriptor(
  name='UACommand',
  full_name='UACommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loadRequests', full_name='UACommand.loadRequests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delivered', full_name='UACommand.delivered', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acks', full_name='UACommand.acks', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='UACommand.error', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=279,
)


_UASTART = _descriptor.Descriptor(
  name='UAstart',
  full_name='UAstart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='UAstart.worldid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UAstart.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=323,
)


_AUPICKUPREQUEST = _descriptor.Descriptor(
  name='AUPickupRequest',
  full_name='AUPickupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='AUPickupRequest.seqNum', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipId', full_name='AUPickupRequest.shipId', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouseId', full_name='AUPickupRequest.warehouseId', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='AUPickupRequest.x', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='AUPickupRequest.y', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destinationX', full_name='AUPickupRequest.destinationX', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destinationY', full_name='AUPickupRequest.destinationY', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=462,
)


_UALOADREQUEST = _descriptor.Descriptor(
  name='UALoadRequest',
  full_name='UALoadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='UALoadRequest.seqNum', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truckId', full_name='UALoadRequest.truckId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipId', full_name='UALoadRequest.shipId', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=528,
)


_AUDELIVERREQUEST = _descriptor.Descriptor(
  name='AUDeliverRequest',
  full_name='AUDeliverRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='AUDeliverRequest.seqNum', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipId', full_name='AUDeliverRequest.shipId', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=580,
)


_UADELIVERED = _descriptor.Descriptor(
  name='UADelivered',
  full_name='UADelivered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='UADelivered.seqNum', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipId', full_name='UADelivered.shipId', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=627,
)


_ERR = _descriptor.Descriptor(
  name='Err',
  full_name='Err',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='Err.err', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originSeqNum', full_name='Err.originSeqNum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='Err.seqNum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=629,
  serialized_end=685,
)

_AUCOMMAND.fields_by_name['pickupRequests'].message_type = _AUPICKUPREQUEST
_AUCOMMAND.fields_by_name['deliverRequests'].message_type = _AUDELIVERREQUEST
_AUCOMMAND.fields_by_name['error'].message_type = _ERR
_UACOMMAND.fields_by_name['loadRequests'].message_type = _UALOADREQUEST
_UACOMMAND.fields_by_name['delivered'].message_type = _UADELIVERED
_UACOMMAND.fields_by_name['error'].message_type = _ERR
DESCRIPTOR.message_types_by_name['AUCommand'] = _AUCOMMAND
DESCRIPTOR.message_types_by_name['UACommand'] = _UACOMMAND
DESCRIPTOR.message_types_by_name['UAstart'] = _UASTART
DESCRIPTOR.message_types_by_name['AUPickupRequest'] = _AUPICKUPREQUEST
DESCRIPTOR.message_types_by_name['UALoadRequest'] = _UALOADREQUEST
DESCRIPTOR.message_types_by_name['AUDeliverRequest'] = _AUDELIVERREQUEST
DESCRIPTOR.message_types_by_name['UADelivered'] = _UADELIVERED
DESCRIPTOR.message_types_by_name['Err'] = _ERR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AUCommand = _reflection.GeneratedProtocolMessageType('AUCommand', (_message.Message,), dict(
  DESCRIPTOR = _AUCOMMAND,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUCommand)
  ))
_sym_db.RegisterMessage(AUCommand)

UACommand = _reflection.GeneratedProtocolMessageType('UACommand', (_message.Message,), dict(
  DESCRIPTOR = _UACOMMAND,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UACommand)
  ))
_sym_db.RegisterMessage(UACommand)

UAstart = _reflection.GeneratedProtocolMessageType('UAstart', (_message.Message,), dict(
  DESCRIPTOR = _UASTART,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UAstart)
  ))
_sym_db.RegisterMessage(UAstart)

AUPickupRequest = _reflection.GeneratedProtocolMessageType('AUPickupRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUPICKUPREQUEST,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUPickupRequest)
  ))
_sym_db.RegisterMessage(AUPickupRequest)

UALoadRequest = _reflection.GeneratedProtocolMessageType('UALoadRequest', (_message.Message,), dict(
  DESCRIPTOR = _UALOADREQUEST,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UALoadRequest)
  ))
_sym_db.RegisterMessage(UALoadRequest)

AUDeliverRequest = _reflection.GeneratedProtocolMessageType('AUDeliverRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUDELIVERREQUEST,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUDeliverRequest)
  ))
_sym_db.RegisterMessage(AUDeliverRequest)

UADelivered = _reflection.GeneratedProtocolMessageType('UADelivered', (_message.Message,), dict(
  DESCRIPTOR = _UADELIVERED,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UADelivered)
  ))
_sym_db.RegisterMessage(UADelivered)

Err = _reflection.GeneratedProtocolMessageType('Err', (_message.Message,), dict(
  DESCRIPTOR = _ERR,
  __module__ = 'protos.amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:Err)
  ))
_sym_db.RegisterMessage(Err)


# @@protoc_insertion_point(module_scope)
