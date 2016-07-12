#!/usr/bin/env python

from __future__ import division # must be first __future__
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
import zmq

def callback(data):
    value = data.r
    # pub.publish(value)
    print("Value: %f" % value)

if __name__ == '__main__':
    rospy.init_node("sub_test", anonymous=True)
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rospy.spin()
