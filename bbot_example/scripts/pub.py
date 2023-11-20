#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('simple_pub_py', anonymous=False)
    pub = rospy.Publisher('talker', String, queue_size=10)
    r = rospy.Rate(10)

    counter = 0
    while not rospy.is_shutdown():
        msgs='Hello World from Pyhton: %d' % counter
        pub.publish(msgs)

        rospy.loginfo(msgs)

        r.sleep()
        counter+=1