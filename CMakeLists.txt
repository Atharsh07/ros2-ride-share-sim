cmake_minimum_required(VERSION 3.5)
project(ros2_ride_share_sim)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

install(PROGRAMS
  ros2_ride_share_sim/rider_node.py
  ros2_ride_share_sim/driver_node.py
  ros2_ride_share_sim/scheduler_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
