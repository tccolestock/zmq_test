#!/usr/bin/env python

""" This example shows how to pass multiple variables to a ROS
 Subscriber object, and how to append the received values to a
 class object attribute.  """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color


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


def fun2():
    print("In other function")
    print(fo.r)
    r = fo.r
    r.append(17)

if __name__ == '__main__':
    rospy.init_node("sub_test", anonymous=True)
    fo = fobar()
    rospy.Subscriber("/turtle1/color_sensor", Color, callback, fo)
    rospy.spin()
