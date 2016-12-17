#!/usr/bin/env python

""" Uses the turtlesim color to test taking data from a
 multipart ZMQ publisher and publishing it to a ROS topic . """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")

rospy.init_node("zmq_turtle_client", anonymous=True)
pub = rospy.Publisher("test_out", Color, queue_size=10)


while not rospy.is_shutdown():
    message = socket.recv_multipart()
    print(len(message))
    color = Color()
    color.r = int(message[0])
    color.g = int(message[1])
    color.b = int(message[2])
    pub.publish(color)
