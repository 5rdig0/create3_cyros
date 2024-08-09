// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice

#ifndef CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__FUNCTIONS_H_
#define CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "create3_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "create3_msgs/msg/detail/armcontrol__struct.h"

/// Initialize msg/Armcontrol message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * create3_msgs__msg__Armcontrol
 * )) before or use
 * create3_msgs__msg__Armcontrol__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
bool
create3_msgs__msg__Armcontrol__init(create3_msgs__msg__Armcontrol * msg);

/// Finalize msg/Armcontrol message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
void
create3_msgs__msg__Armcontrol__fini(create3_msgs__msg__Armcontrol * msg);

/// Create msg/Armcontrol message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * create3_msgs__msg__Armcontrol__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
create3_msgs__msg__Armcontrol *
create3_msgs__msg__Armcontrol__create();

/// Destroy msg/Armcontrol message.
/**
 * It calls
 * create3_msgs__msg__Armcontrol__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
void
create3_msgs__msg__Armcontrol__destroy(create3_msgs__msg__Armcontrol * msg);

/// Check for msg/Armcontrol message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
bool
create3_msgs__msg__Armcontrol__are_equal(const create3_msgs__msg__Armcontrol * lhs, const create3_msgs__msg__Armcontrol * rhs);

/// Copy a msg/Armcontrol message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
bool
create3_msgs__msg__Armcontrol__copy(
  const create3_msgs__msg__Armcontrol * input,
  create3_msgs__msg__Armcontrol * output);

/// Initialize array of msg/Armcontrol messages.
/**
 * It allocates the memory for the number of elements and calls
 * create3_msgs__msg__Armcontrol__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
bool
create3_msgs__msg__Armcontrol__Sequence__init(create3_msgs__msg__Armcontrol__Sequence * array, size_t size);

/// Finalize array of msg/Armcontrol messages.
/**
 * It calls
 * create3_msgs__msg__Armcontrol__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
void
create3_msgs__msg__Armcontrol__Sequence__fini(create3_msgs__msg__Armcontrol__Sequence * array);

/// Create array of msg/Armcontrol messages.
/**
 * It allocates the memory for the array and calls
 * create3_msgs__msg__Armcontrol__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
create3_msgs__msg__Armcontrol__Sequence *
create3_msgs__msg__Armcontrol__Sequence__create(size_t size);

/// Destroy array of msg/Armcontrol messages.
/**
 * It calls
 * create3_msgs__msg__Armcontrol__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
void
create3_msgs__msg__Armcontrol__Sequence__destroy(create3_msgs__msg__Armcontrol__Sequence * array);

/// Check for msg/Armcontrol message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
bool
create3_msgs__msg__Armcontrol__Sequence__are_equal(const create3_msgs__msg__Armcontrol__Sequence * lhs, const create3_msgs__msg__Armcontrol__Sequence * rhs);

/// Copy an array of msg/Armcontrol messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_create3_msgs
bool
create3_msgs__msg__Armcontrol__Sequence__copy(
  const create3_msgs__msg__Armcontrol__Sequence * input,
  create3_msgs__msg__Armcontrol__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__FUNCTIONS_H_
