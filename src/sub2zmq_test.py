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
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

geo_encode = geometry_msgs.Encode()

def callback(data):
    msg = geo_encode.accel_stamped(data)
    packed = msgpack.dumps(msg)
    socket.send(packed)
    print("sent...")

def listen():
    rospy.init_node("test_node", anonymous=True)
    rospy.Subscriber("/test_pub", AccelStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listen()
