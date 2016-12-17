#!/usr/bin/env python

""" Uses the turtlesim color to test taking data from ROS
 and pushing it to ZMQ by using pickle to serialize the
 Python ROS message object types. """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import cPickle as pickle

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


def callback(data):
    print(data)
    pickled = pickle.dumps(data, -1)
    print("pickling.... \n")
    socket.send(pickled)


def listen():
    rospy.init_node("zmq_turtle_server", anonymous=True)
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rospy.spin()


if __name__ == '__main__':
    listen()
