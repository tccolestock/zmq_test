#!/usr/bin/env python

""" Connects to a ZMQ socket that has received a serialized turtlesim
 Color, then deserializes it using Pickle and publishes it to a ROS
 topic (/test_out). """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import time
import cPickle as pickle

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")


def talker():
    rospy.init_node("zmq_turtle_client", anonymous=True)
    pub = rospy.Publisher("test_out", Color, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500)  # hz

    while not rospy.is_shutdown():
        message = socket.recv()
        print("received")
        data = pickle.loads(message)
        print("unpickled")
        pub.publish(data)
        print("published")
        rate_handle.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
