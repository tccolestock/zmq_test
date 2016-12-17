#!/usr/bin/env python

""" Uses the turtlesim color to test taking data from ros
 and pushing it to zmq through a multipart zmq publisher."""

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

rospy.init_node("zmq_turtle_server", anonymous=True)
rate = rospy.Rate(1)  # hz


def callback(data):
    socket.send_multipart([b"%03d" % data.r, b"%03d"
                          % data.g, b"%03d" % data.b])


while not rospy.is_shutdown():
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rate.sleep()
