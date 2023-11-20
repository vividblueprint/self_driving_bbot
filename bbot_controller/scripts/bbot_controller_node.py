#!/usr/bin/env python3
import rospy
from bbot_controller.bbot_controller import Bbot_controller

if __name__ == '__main__':
    rospy.init_node('bbot_controller')
    wheel_radius = rospy.get_param("~wheel_radius")
    wheel_separation = rospy.get_param("~wheel_separation")
    bbot_controller = Bbot_controller(wheel_radius,wheel_separation)

    rospy.spin()