// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from turtlesim_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice

#ifndef TURTLESIM_INTERFACES__SRV__DETAIL__SEND_POSITION__STRUCT_HPP_
#define TURTLESIM_INTERFACES__SRV__DETAIL__SEND_POSITION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__turtlesim_interfaces__srv__SendPosition_Request __attribute__((deprecated))
#else
# define DEPRECATED__turtlesim_interfaces__srv__SendPosition_Request __declspec(deprecated)
#endif

namespace turtlesim_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SendPosition_Request_
{
  using Type = SendPosition_Request_<ContainerAllocator>;

  explicit SendPosition_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_init)
  {
    (void)_init;
  }

  explicit SendPosition_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _position_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _position_type position;

  // setters for named parameter idiom
  Type & set__position(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->position = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlesim_interfaces__srv__SendPosition_Request
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlesim_interfaces__srv__SendPosition_Request
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendPosition_Request_ & other) const
  {
    if (this->position != other.position) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendPosition_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendPosition_Request_

// alias to use template instance with default allocator
using SendPosition_Request =
  turtlesim_interfaces::srv::SendPosition_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtlesim_interfaces


#ifndef _WIN32
# define DEPRECATED__turtlesim_interfaces__srv__SendPosition_Response __attribute__((deprecated))
#else
# define DEPRECATED__turtlesim_interfaces__srv__SendPosition_Response __declspec(deprecated)
#endif

namespace turtlesim_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SendPosition_Response_
{
  using Type = SendPosition_Response_<ContainerAllocator>;

  explicit SendPosition_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit SendPosition_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlesim_interfaces__srv__SendPosition_Response
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlesim_interfaces__srv__SendPosition_Response
    std::shared_ptr<turtlesim_interfaces::srv::SendPosition_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendPosition_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendPosition_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendPosition_Response_

// alias to use template instance with default allocator
using SendPosition_Response =
  turtlesim_interfaces::srv::SendPosition_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtlesim_interfaces

namespace turtlesim_interfaces
{

namespace srv
{

struct SendPosition
{
  using Request = turtlesim_interfaces::srv::SendPosition_Request;
  using Response = turtlesim_interfaces::srv::SendPosition_Response;
};

}  // namespace srv

}  // namespace turtlesim_interfaces

#endif  // TURTLESIM_INTERFACES__SRV__DETAIL__SEND_POSITION__STRUCT_HPP_
