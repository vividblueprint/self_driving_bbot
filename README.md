# Clone the repo
```
https://github.com/vividblueprint/self_driving_bbot.git
```

# Launch the Gazebo simulation
```
roslaunch bbot_sim gazebo_bbot.launch
```

# Autonomous Navigation

1. Sensor Fusion
1. Kalman Filter
1. Probability Theory
1. Robot Kinematics
1. Odometry
1. Robot Localization
1. Control

### To prepare your PC you need:

- Install Ubuntu 20.04 on PC or in Virtual Machine Download the ISO Ubuntu 20.04 for your PC
- Install ROS Noetic on your Ubuntu 20.04
- Install ROS missing libraries. Some libraries that are used in this project are not in the standard ROS package. Install them with:

```
sudo apt-get update && sudo apt-get install -y \
     ros-noetic-ros-controllers \
     ros-noetic-gazebo-ros-control \
     ros-noetic-joint-state-publisher-gui \
     ros-noetic-joy \
     ros-noetic-joy-teleop \
     ros-noetic-turtlesim \
     ros-noetic-robot-localization \
     ros-noetic-actionlib-tools
```
