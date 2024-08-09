// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from create3_msgs:msg/Armcontrol.idl
// generated code does not contain a copyright notice

#ifndef CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__BUILDER_HPP_
#define CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "create3_msgs/msg/detail/armcontrol__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace create3_msgs
{

namespace msg
{

namespace builder
{

class Init_Armcontrol_command
{
public:
  explicit Init_Armcontrol_command(::create3_msgs::msg::Armcontrol & msg)
  : msg_(msg)
  {}
  ::create3_msgs::msg::Armcontrol command(::create3_msgs::msg::Armcontrol::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::create3_msgs::msg::Armcontrol msg_;
};

class Init_Armcontrol_speed
{
public:
  explicit Init_Armcontrol_speed(::create3_msgs::msg::Armcontrol & msg)
  : msg_(msg)
  {}
  Init_Armcontrol_command speed(::create3_msgs::msg::Armcontrol::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_Armcontrol_command(msg_);
  }

private:
  ::create3_msgs::msg::Armcontrol msg_;
};

class Init_Armcontrol_time
{
public:
  explicit Init_Armcontrol_time(::create3_msgs::msg::Armcontrol & msg)
  : msg_(msg)
  {}
  Init_Armcontrol_speed time(::create3_msgs::msg::Armcontrol::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_Armcontrol_speed(msg_);
  }

private:
  ::create3_msgs::msg::Armcontrol msg_;
};

class Init_Armcontrol_pos
{
public:
  Init_Armcontrol_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Armcontrol_time pos(::create3_msgs::msg::Armcontrol::_pos_type arg)
  {
    msg_.pos = std::move(arg);
    return Init_Armcontrol_time(msg_);
  }

private:
  ::create3_msgs::msg::Armcontrol msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::create3_msgs::msg::Armcontrol>()
{
  return create3_msgs::msg::builder::Init_Armcontrol_pos();
}

}  // namespace create3_msgs

#endif  // CREATE3_MSGS__MSG__DETAIL__ARMCONTROL__BUILDER_HPP_
