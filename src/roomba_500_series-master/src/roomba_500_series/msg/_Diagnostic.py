"""autogenerated by genpy from roomba_500_series/Diagnostic.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Diagnostic(genpy.Message):
  _md5sum = "c5ab1a026621d8d87d7316b146c2ca2a"
  _type = "roomba_500_series/Diagnostic"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
int16 left_motor_current
int16 right_motor_current
int16 main_brush_current
int16 side_brush_current
bool left_motor_overcurrent
bool right_motor_overcurrent
bool main_brush_overcurrent
bool side_brush_overcurrent
int16 battery_current
int16 battery_voltage
int8 battery_temperature

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','left_motor_current','right_motor_current','main_brush_current','side_brush_current','left_motor_overcurrent','right_motor_overcurrent','main_brush_overcurrent','side_brush_overcurrent','battery_current','battery_voltage','battery_temperature']
  _slot_types = ['std_msgs/Header','int16','int16','int16','int16','bool','bool','bool','bool','int16','int16','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,left_motor_current,right_motor_current,main_brush_current,side_brush_current,left_motor_overcurrent,right_motor_overcurrent,main_brush_overcurrent,side_brush_overcurrent,battery_current,battery_voltage,battery_temperature

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Diagnostic, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.left_motor_current is None:
        self.left_motor_current = 0
      if self.right_motor_current is None:
        self.right_motor_current = 0
      if self.main_brush_current is None:
        self.main_brush_current = 0
      if self.side_brush_current is None:
        self.side_brush_current = 0
      if self.left_motor_overcurrent is None:
        self.left_motor_overcurrent = False
      if self.right_motor_overcurrent is None:
        self.right_motor_overcurrent = False
      if self.main_brush_overcurrent is None:
        self.main_brush_overcurrent = False
      if self.side_brush_overcurrent is None:
        self.side_brush_overcurrent = False
      if self.battery_current is None:
        self.battery_current = 0
      if self.battery_voltage is None:
        self.battery_voltage = 0
      if self.battery_temperature is None:
        self.battery_temperature = 0
    else:
      self.header = std_msgs.msg.Header()
      self.left_motor_current = 0
      self.right_motor_current = 0
      self.main_brush_current = 0
      self.side_brush_current = 0
      self.left_motor_overcurrent = False
      self.right_motor_overcurrent = False
      self.main_brush_overcurrent = False
      self.side_brush_overcurrent = False
      self.battery_current = 0
      self.battery_voltage = 0
      self.battery_temperature = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4h4B2hb.pack(_x.left_motor_current, _x.right_motor_current, _x.main_brush_current, _x.side_brush_current, _x.left_motor_overcurrent, _x.right_motor_overcurrent, _x.main_brush_overcurrent, _x.side_brush_overcurrent, _x.battery_current, _x.battery_voltage, _x.battery_temperature))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 17
      (_x.left_motor_current, _x.right_motor_current, _x.main_brush_current, _x.side_brush_current, _x.left_motor_overcurrent, _x.right_motor_overcurrent, _x.main_brush_overcurrent, _x.side_brush_overcurrent, _x.battery_current, _x.battery_voltage, _x.battery_temperature,) = _struct_4h4B2hb.unpack(str[start:end])
      self.left_motor_overcurrent = bool(self.left_motor_overcurrent)
      self.right_motor_overcurrent = bool(self.right_motor_overcurrent)
      self.main_brush_overcurrent = bool(self.main_brush_overcurrent)
      self.side_brush_overcurrent = bool(self.side_brush_overcurrent)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4h4B2hb.pack(_x.left_motor_current, _x.right_motor_current, _x.main_brush_current, _x.side_brush_current, _x.left_motor_overcurrent, _x.right_motor_overcurrent, _x.main_brush_overcurrent, _x.side_brush_overcurrent, _x.battery_current, _x.battery_voltage, _x.battery_temperature))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 17
      (_x.left_motor_current, _x.right_motor_current, _x.main_brush_current, _x.side_brush_current, _x.left_motor_overcurrent, _x.right_motor_overcurrent, _x.main_brush_overcurrent, _x.side_brush_overcurrent, _x.battery_current, _x.battery_voltage, _x.battery_temperature,) = _struct_4h4B2hb.unpack(str[start:end])
      self.left_motor_overcurrent = bool(self.left_motor_overcurrent)
      self.right_motor_overcurrent = bool(self.right_motor_overcurrent)
      self.main_brush_overcurrent = bool(self.main_brush_overcurrent)
      self.side_brush_overcurrent = bool(self.side_brush_overcurrent)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4h4B2hb = struct.Struct("<4h4B2hb")
_struct_3I = struct.Struct("<3I")
