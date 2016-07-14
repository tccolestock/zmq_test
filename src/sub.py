#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from sensor_msgs.msg import JointState

rospy.init_node("test_sub", anonymous=True)

def callback(data):
    print("in callback")
    print(data)

# if __name__ == '__main__':
while not rospy.is_shutdown():

    print("before sub")
    rospy.Subscriber("/test_out", JointState, callback)
    print("after sub")
    # rospy.spin()
    print("after spin")
