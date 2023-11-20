#!/usr/bin/env python3
import rospy
from bbot_example.turtlesim_kinematics import TurtlesimKinematics


if __name__== '__main__':
    rospy.init_node('turtlesim_kinematics_node')
    turtlesim_kinematics = TurtlesimKinematics()

    rospy.spin()