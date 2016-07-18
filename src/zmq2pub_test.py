#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
import zmq
import msgpack
from rospy_msgpack import turtlesim, geometry_msgs
from geometry_msgs.msg import AccelStamped

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://*:5555")

geo_decode = geometry_msgs.Decode()

def talker():
    rospy.init_node("z2pub", anonymous=True)
    pub = rospy.Publisher("test2", AccelStamped, queue_size=10)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
