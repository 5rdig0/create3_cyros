// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice
#include "create3_msgs/msg/detail/armcontrol__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

bool
create3_msgs__msg__Armcontrol__init(create3_msgs__msg__Armcontrol * msg)
{
  if (!msg) {
    return false;
  }
  // pos
  // time
  // speed
  // command
  if (!rosidl_runtime_c__String__init(&msg->command)) {
    create3_msgs__msg__Armcontrol__fini(msg);
    return false;
  }
  return true;
}

void
create3_msgs__msg__Armcontrol__fini(create3_msgs__msg__Armcontrol * msg)
{
  if (!msg) {
    return;
  }
  // pos
  // time
  // speed
  // command
  rosidl_runtime_c__String__fini(&msg->command);
}

bool
create3_msgs__msg__Armcontrol__are_equal(const create3_msgs__msg__Armcontrol * lhs, const create3_msgs__msg__Armcontrol * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // pos
  if (lhs->pos != rhs->pos) {
    return false;
  }
  // time
  if (lhs->time != rhs->time) {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->command), &(rhs->command)))
  {
    return false;
  }
  return true;
}

bool
create3_msgs__msg__Armcontrol__copy(
  const create3_msgs__msg__Armcontrol * input,
  create3_msgs__msg__Armcontrol * output)
{
  if (!input || !output) {
    return false;
  }
  // pos
  output->pos = input->pos;
  // time
  output->time = input->time;
  // speed
  output->speed = input->speed;
  // command
  if (!rosidl_runtime_c__String__copy(
      &(input->command), &(output->command)))
  {
    return false;
  }
  return true;
}

create3_msgs__msg__Armcontrol *
create3_msgs__msg__Armcontrol__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  create3_msgs__msg__Armcontrol * msg = (create3_msgs__msg__Armcontrol *)allocator.allocate(sizeof(create3_msgs__msg__Armcontrol), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(create3_msgs__msg__Armcontrol));
  bool success = create3_msgs__msg__Armcontrol__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
create3_msgs__msg__Armcontrol__destroy(create3_msgs__msg__Armcontrol * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    create3_msgs__msg__Armcontrol__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
create3_msgs__msg__Armcontrol__Sequence__init(create3_msgs__msg__Armcontrol__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  create3_msgs__msg__Armcontrol * data = NULL;

  if (size) {
    data = (create3_msgs__msg__Armcontrol *)allocator.zero_allocate(size, sizeof(create3_msgs__msg__Armcontrol), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = create3_msgs__msg__Armcontrol__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        create3_msgs__msg__Armcontrol__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
create3_msgs__msg__Armcontrol__Sequence__fini(create3_msgs__msg__Armcontrol__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      create3_msgs__msg__Armcontrol__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

create3_msgs__msg__Armcontrol__Sequence *
create3_msgs__msg__Armcontrol__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  create3_msgs__msg__Armcontrol__Sequence * array = (create3_msgs__msg__Armcontrol__Sequence *)allocator.allocate(sizeof(create3_msgs__msg__Armcontrol__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = create3_msgs__msg__Armcontrol__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
create3_msgs__msg__Armcontrol__Sequence__destroy(create3_msgs__msg__Armcontrol__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    create3_msgs__msg__Armcontrol__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
create3_msgs__msg__Armcontrol__Sequence__are_equal(const create3_msgs__msg__Armcontrol__Sequence * lhs, const create3_msgs__msg__Armcontrol__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!create3_msgs__msg__Armcontrol__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
create3_msgs__msg__Armcontrol__Sequence__copy(
  const create3_msgs__msg__Armcontrol__Sequence * input,
  create3_msgs__msg__Armcontrol__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(create3_msgs__msg__Armcontrol);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    create3_msgs__msg__Armcontrol * data =
      (create3_msgs__msg__Armcontrol *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!create3_msgs__msg__Armcontrol__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          create3_msgs__msg__Armcontrol__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!create3_msgs__msg__Armcontrol__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
