// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "create3_msgs/msg/detail/armcontrol__rosidl_typesupport_introspection_c.h"
#include "create3_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "create3_msgs/msg/detail/armcontrol__functions.h"
#include "create3_msgs/msg/detail/armcontrol__struct.h"


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  create3_msgs__msg__Armcontrol__init(message_memory);
}

void create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_fini_function(void * message_memory)
{
  create3_msgs__msg__Armcontrol__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_member_array[4] = {
  {
    "pos",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(create3_msgs__msg__Armcontrol, pos),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(create3_msgs__msg__Armcontrol, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(create3_msgs__msg__Armcontrol, speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(create3_msgs__msg__Armcontrol, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_members = {
  "create3_msgs__msg",  // message namespace
  "Armcontrol",  // message name
  4,  // number of fields
  sizeof(create3_msgs__msg__Armcontrol),
  create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_member_array,  // message members
  create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_init_function,  // function to initialize message memory (memory has to be allocated)
  create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_type_support_handle = {
  0,
  &create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_create3_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, create3_msgs, msg, Armcontrol)() {
  if (!create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_type_support_handle.typesupport_identifier) {
    create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &create3_msgs__msg__Armcontrol__rosidl_typesupport_introspection_c__Armcontrol_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
