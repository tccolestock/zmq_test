#!/usr/bin/env python

""" Shows how to us a general form of the ZMQ Request protocol.
 Also shows how a request can be made, and the returned data can
 be put into a ROS topic by a ROS Publisher. """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import time

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def talker():
    rospy.init_node("zmq_request", anonymous=True)
    pub = rospy.Publisher("req_out", Float32, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500)  # hz

    while not rospy.is_shutdown():
        socket.send(b"now")
        msg = socket.recv_string()
        msg = float(msg)
        print(msg)
        pub.publish(msg)
        rate_handle.sleep()


if __name__ == '__main__':
    talker()
