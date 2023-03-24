# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sophon_robot/Frame.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import sophon_robot.msg
import std_msgs.msg

class Frame(genpy.Message):
  _md5sum = "c73f23c5150c19b07c35b376f304e421"
  _type = "sophon_robot/Frame"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 frame_id
sensor_msgs/CompressedImage img
Bboxes bboxes
================================================================================
MSG: sensor_msgs/CompressedImage
# This message contains a compressed image

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image

string format        # Specifies the format of the data
                     #   Acceptable values:
                     #     jpeg, png
uint8[] data         # Compressed image buffer

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sophon_robot/Bboxes
uint32 frame_id
uint32 num_object
Bbox[] bboxes

================================================================================
MSG: sophon_robot/Bbox
uint32 frame_id
uint32 object_id 
int32  track_id
string object_name
float32  left_top_x
float32  left_top_y
float32  width
float32  height
float32  conf"""
  __slots__ = ['frame_id','img','bboxes']
  _slot_types = ['uint32','sensor_msgs/CompressedImage','sophon_robot/Bboxes']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       frame_id,img,bboxes

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Frame, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.frame_id is None:
        self.frame_id = 0
      if self.img is None:
        self.img = sensor_msgs.msg.CompressedImage()
      if self.bboxes is None:
        self.bboxes = sophon_robot.msg.Bboxes()
    else:
      self.frame_id = 0
      self.img = sensor_msgs.msg.CompressedImage()
      self.bboxes = sophon_robot.msg.Bboxes()

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
      buff.write(_get_struct_4I().pack(_x.frame_id, _x.img.header.seq, _x.img.header.stamp.secs, _x.img.header.stamp.nsecs))
      _x = self.img.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.img.format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.img.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.bboxes.frame_id, _x.bboxes.num_object))
      length = len(self.bboxes.bboxes)
      buff.write(_struct_I.pack(length))
      for val1 in self.bboxes.bboxes:
        _x = val1
        buff.write(_get_struct_2Ii().pack(_x.frame_id, _x.object_id, _x.track_id))
        _x = val1.object_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_5f().pack(_x.left_top_x, _x.left_top_y, _x.width, _x.height, _x.conf))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.img is None:
        self.img = sensor_msgs.msg.CompressedImage()
      if self.bboxes is None:
        self.bboxes = sophon_robot.msg.Bboxes()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.frame_id, _x.img.header.seq, _x.img.header.stamp.secs, _x.img.header.stamp.nsecs,) = _get_struct_4I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.img.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.img.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.img.format = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.img.format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.img.data = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.bboxes.frame_id, _x.bboxes.num_object,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bboxes.bboxes = []
      for i in range(0, length):
        val1 = sophon_robot.msg.Bbox()
        _x = val1
        start = end
        end += 12
        (_x.frame_id, _x.object_id, _x.track_id,) = _get_struct_2Ii().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.object_name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.object_name = str[start:end]
        _x = val1
        start = end
        end += 20
        (_x.left_top_x, _x.left_top_y, _x.width, _x.height, _x.conf,) = _get_struct_5f().unpack(str[start:end])
        self.bboxes.bboxes.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4I().pack(_x.frame_id, _x.img.header.seq, _x.img.header.stamp.secs, _x.img.header.stamp.nsecs))
      _x = self.img.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.img.format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.img.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.bboxes.frame_id, _x.bboxes.num_object))
      length = len(self.bboxes.bboxes)
      buff.write(_struct_I.pack(length))
      for val1 in self.bboxes.bboxes:
        _x = val1
        buff.write(_get_struct_2Ii().pack(_x.frame_id, _x.object_id, _x.track_id))
        _x = val1.object_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_5f().pack(_x.left_top_x, _x.left_top_y, _x.width, _x.height, _x.conf))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.img is None:
        self.img = sensor_msgs.msg.CompressedImage()
      if self.bboxes is None:
        self.bboxes = sophon_robot.msg.Bboxes()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.frame_id, _x.img.header.seq, _x.img.header.stamp.secs, _x.img.header.stamp.nsecs,) = _get_struct_4I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.img.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.img.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.img.format = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.img.format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.img.data = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.bboxes.frame_id, _x.bboxes.num_object,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bboxes.bboxes = []
      for i in range(0, length):
        val1 = sophon_robot.msg.Bbox()
        _x = val1
        start = end
        end += 12
        (_x.frame_id, _x.object_id, _x.track_id,) = _get_struct_2Ii().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.object_name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.object_name = str[start:end]
        _x = val1
        start = end
        end += 20
        (_x.left_top_x, _x.left_top_y, _x.width, _x.height, _x.conf,) = _get_struct_5f().unpack(str[start:end])
        self.bboxes.bboxes.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2Ii = None
def _get_struct_2Ii():
    global _struct_2Ii
    if _struct_2Ii is None:
        _struct_2Ii = struct.Struct("<2Ii")
    return _struct_2Ii
_struct_4I = None
def _get_struct_4I():
    global _struct_4I
    if _struct_4I is None:
        _struct_4I = struct.Struct("<4I")
    return _struct_4I
_struct_5f = None
def _get_struct_5f():
    global _struct_5f
    if _struct_5f is None:
        _struct_5f = struct.Struct("<5f")
    return _struct_5f
