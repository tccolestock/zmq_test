#!/usr/bin/env python

""" Shows a general form of using the ZMQ Reply protocol. Also,
 showcases how a ROS topic's data can be retrieved through a
 subscriber and returned as the ZMQ reply. """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import time

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from sensor_msgs.msg import JointState


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def callback(data):
    d = data.position[1]
    message = socket.recv()
    if message == "now":
        socket.send_string(b"%03f" % d)
        print(d)
        message = ""


def listen():
    rospy.init_node("zmq_reply", anonymous=True)
    rospy.Subscriber("/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listen()
