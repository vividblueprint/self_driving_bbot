#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("New msg received: %s"%msg.data)

if __name__ == '__main__':
    rospy.init_node('simple_sub_py', anonymous=False)
    pub = rospy.Subscriber('talker', String,callback=callback)

    rospy.spin()
