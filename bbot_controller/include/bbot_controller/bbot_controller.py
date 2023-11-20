#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

class Bbot_controller(object):

    def __init__(self, wheel_radius, wheel_separation):
        rospy.loginfo("Using wheel radius %d"%wheel_radius)
        rospy.loginfo("Using wheel separation %d"%wheel_separation)

        self.left_cmd_pub_ = rospy.Publisher("wheel_left_controller/command", Float64, queue_size=10)
        self.right_cmd_pub_ = rospy.Publisher("wheel_right_controller/command",Float64, queue_size=10)
        self.vel_sub_ = rospy.Subscriber("bbot_controller/cmd_vel", Twist, self.velCallBack)
        self.speed_conversion_ = np.array([[wheel_radius/2, wheel_radius/2],[wheel_radius/wheel_separation, -wheel_radius/wheel_separation]])
        
        rospy.loginfo("Convirsion matrix is %s"%self.speed_conversion_)

    def velCallBack(self, msg):
        bbot_speed = np.array([[msg.linear.x],[msg.angular.z]])
        wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion_),bbot_speed)
        
        left_wheel_speed = Float64(wheel_speed[1,0])
        right_wheel_speed = Float64(wheel_speed[0,0])

        self.left_cmd_pub_.publish(left_wheel_speed)
        self.right_cmd_pub_.publish(right_wheel_speed)