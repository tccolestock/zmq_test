#!/usr/bin/env python

from __future__ import division # must be first __future__
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
import zmq


class fobar(object):
    """docstring for fobar"""
    def __init__(self, ):
        self.r = []
        self.g = 0
        self.b = 0





def callback(data, c):
    print("First in method")
    print(c.r)

    value = data.r
    c.r.append(value)
    print("Second in method")
    print(c.r)
    fun2()
    # pub.publish(value)
    # print("Value: %f" % value)

def fun2():
    print("In other function")
    print(fo.r)
    # x = fo.r
    # print("x: %s" % x)
    r = fo.r
    r.append(17)

if __name__ == '__main__':
    rospy.init_node("sub_test", anonymous=True)
    fo = fobar()
    rospy.Subscriber("/turtle1/color_sensor", Color, callback, fo)
    rospy.spin()
