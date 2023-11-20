
<p align="center">
  <a href="https://github.com/vividblueprint/self_driving_bbot/actions">
    <img alt="Tests Passing" src="https://github.com/anuraghazra/github-readme-stats/workflows/Test/badge.svg"/>
  </a>
  <a href="https://github.com/vividblueprint/self_driving_bbot/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/vividblueprint/self_driving_bbot"/>
  </a>
  <a href="https://github.com/vividblueprint/self_driving_bbot/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/vividblueprint/self_driving_bbot?color=0088ff"/>
  </a>
  <a href="https://github.com/vividblueprint/self_driving_bbot/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/vividblueprint/self_driving_bbot?color=0088ff">
  </a>
  <br />
<img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/vividblueprint/self_driving_bbot?color=green">
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/vividblueprint/self_driving_bbot?color=302df0">
<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/vividblueprint/self_driving_bbot">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/vividblueprint/self_driving_bbot?color=0088ff">
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/vividblueprint/self_driving_bbot?color=00ff00f">
<img alt="GitHub repo file count" src="https://img.shields.io/github/directory-file-count/vividblueprint/self_driving_bbot">
</p>


# Clone the repo
```
git clone https://github.com/vividblueprint/self_driving_bbot.git
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
