#!/usr/bin/env python

""" Uses the turtlesim command velocity to test taking data
 from ros and pushing it to ZMQ. Utilizes the rospy_msgpack
 library (custom built) to convert the ROS message type into
 a form that is serializable by msgpack."""

from __future__ import division

# These must come after __future__
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy
import zmq
import msgpack

from std_msgs.msg import String, Float32, UInt8
from geometry_msgs.msg import Twist, Polygon, PoseArray
from rospy_msgpack import geometry_msgpack


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Create encoding objects from rospy_msgpack library
geo_encode = geometry_msgpack.Encode()


def callback(velo):
    print("in callback")
    msg = geo_encode.twist(velo)  # convert to serializable form
    print(msg)
    packed = msgpack.dumps(msg)  # serialize with msgpack
    socket.send(packed)  # send to socket over ZMQ


def listen():
    rospy.init_node("zmq_server", anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    rospy.spin()


if __name__ == '__main__':
    listen()
