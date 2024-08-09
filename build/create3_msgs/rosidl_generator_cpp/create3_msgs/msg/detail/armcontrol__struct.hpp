// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice

#ifndef CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__STRUCT_HPP_
#define CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__create3_msgs__msg__Armcontrol __attribute__((deprecated))
#else
# define DEPRECATED__create3_msgs__msg__Armcontrol __declspec(deprecated)
#endif

namespace create3_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Armcontrol_
{
  using Type = Armcontrol_<ContainerAllocator>;

  explicit Armcontrol_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos = 0;
      this->time = 0;
      this->speed = 0;
      this->command = "";
    }
  }

  explicit Armcontrol_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos = 0;
      this->time = 0;
      this->speed = 0;
      this->command = "";
    }
  }

  // field types and members
  using _pos_type =
    int16_t;
  _pos_type pos;
  using _time_type =
    int16_t;
  _time_type time;
  using _speed_type =
    int16_t;
  _speed_type speed;
  using _command_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _command_type command;

  // setters for named parameter idiom
  Type & set__pos(
    const int16_t & _arg)
  {
    this->pos = _arg;
    return *this;
  }
  Type & set__time(
    const int16_t & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__speed(
    const int16_t & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__command(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    create3_msgs::msg::Armcontrol_<ContainerAllocator> *;
  using ConstRawPtr =
    const create3_msgs::msg::Armcontrol_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      create3_msgs::msg::Armcontrol_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      create3_msgs::msg::Armcontrol_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__create3_msgs__msg__Armcontrol
    std::shared_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__create3_msgs__msg__Armcontrol
    std::shared_ptr<create3_msgs::msg::Armcontrol_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Armcontrol_ & other) const
  {
    if (this->pos != other.pos) {
      return false;
    }
    if (this->time != other.time) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const Armcontrol_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Armcontrol_

// alias to use template instance with default allocator
using Armcontrol =
  create3_msgs::msg::Armcontrol_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace create3_msgs

#endif  // CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__STRUCT_HPP_
