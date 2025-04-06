## JdeRobot GSoC 2025
This repository contains a well documented code for Part 1(a) of JdeRobot's GSoC 2025 ROS2 Test

### Aim
- Create a new ROS2 workspace
- Create ROS2 publisher-subscriber nodes and publish the message ‘Hello! ROS2 is fun.’
- Build the package using colcon
- Use ROS2 run for executable

### Requirements

- Ubuntu 22.04
- ROS2 Humble

### Setup

1. Clone this repository:
   ```sh
   git clone git@github.com:ShauryaJain03/jderobot_intro.git
   cd jderobot_intro
   colcon build
   ```
   
2. Install dependencies and build with colcon again
   ```sh
   rosdep install --from-paths src --ignore-src -r -y
   colcon build
   ```

### Usage

Source workspace and run the Publisher Node

   ```sh
   source install/setup.bash
   ros2 run intro publisher
   ```
Source workspace and run the Subscriber Node
   ```sh
   source install/setup.bash
   ros2 run intro subscriber
   ```

### Demo
- The accompanying video of the result can be found at - https://youtu.be/WD3yewwLf-8
- The video for Part 2 of ROS2 Test can be found at - https://youtu.be/fcoYAeJ6mxw

