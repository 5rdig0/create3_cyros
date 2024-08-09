// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice

#ifndef CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__TRAITS_HPP_
#define CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "create3_msgs/msg/detail/armcontrol__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace create3_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Armcontrol & msg,
  std::ostream & out)
{
  out << "{";
  // member: pos
  {
    out << "pos: ";
    rosidl_generator_traits::value_to_yaml(msg.pos, out);
    out << ", ";
  }

  // member: time
  {
    out << "time: ";
    rosidl_generator_traits::value_to_yaml(msg.time, out);
    out << ", ";
  }

  // member: speed
  {
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << ", ";
  }

  // member: command
  {
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Armcontrol & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos: ";
    rosidl_generator_traits::value_to_yaml(msg.pos, out);
    out << "\n";
  }

  // member: time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time: ";
    rosidl_generator_traits::value_to_yaml(msg.time, out);
    out << "\n";
  }

  // member: speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << "\n";
  }

  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Armcontrol & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace create3_msgs

namespace rosidl_generator_traits
{

[[deprecated("use create3_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const create3_msgs::msg::Armcontrol & msg,
  std::ostream & out, size_t indentation = 0)
{
  create3_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use create3_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const create3_msgs::msg::Armcontrol & msg)
{
  return create3_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<create3_msgs::msg::Armcontrol>()
{
  return "create3_msgs::msg::Armcontrol";
}

template<>
inline const char * name<create3_msgs::msg::Armcontrol>()
{
  return "create3_msgs/msg/Armcontrol";
}

template<>
struct has_fixed_size<create3_msgs::msg::Armcontrol>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<create3_msgs::msg::Armcontrol>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<create3_msgs::msg::Armcontrol>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__TRAITS_HPP_
