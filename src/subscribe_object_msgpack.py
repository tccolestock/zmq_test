#!/usr/bin/env python

""" Subscribes to a ZMQ socket, and uses msgpack to deserialize,
 then rospy_msgpack to convert back into an appropriate ROS msg
 format. """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy
import time
import zmq
import msgpack

from std_msgs.msg import String, Float32, UInt8
from geometry_msgs.msg import Twist
from rospy_msgpack import geometry_msgpack


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")

# Create decoding objects
geo_decode = geometry_msgpack.Decode()


def talker():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("test_velo", Twist, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500)  # hz

    while not rospy.is_shutdown():
        rec = socket.recv()
        msg = msgpack.loads(rec)
        velo = Twist()
        velo = geo_decode.twist(msg, velo)
        print(velo)
        pub.publish(velo)
        rate_handle.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
