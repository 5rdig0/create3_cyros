// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice

#ifndef CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__STRUCT_H_
#define CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Armcontrol in the package create3_msgs.
typedef struct create3_msgs__msg__Armcontrol
{
  int16_t pos;
  int16_t time;
  int16_t speed;
  rosidl_runtime_c__String command;
} create3_msgs__msg__Armcontrol;

// Struct for a sequence of create3_msgs__msg__Armcontrol.
typedef struct create3_msgs__msg__Armcontrol__Sequence
{
  create3_msgs__msg__Armcontrol * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} create3_msgs__msg__Armcontrol__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__STRUCT_H_
