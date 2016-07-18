#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
import zmq
import msgpack
from rospy_msgpack import sensor_msgs
from rospy_msgpack import turtlesim

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Create encoding objects
sensor_encode = sensor_msgs.Encode()
turtle_encode = turtlesim.Encode()

def callback(color):
    msg = turtle_encode.color(color)
    print(msg)
    packed = msgpack.dumps(msg)
    socket.send(packed)

def callback2(state):
    msg = sensor_encode.joint_state(state)
    print(msg)
    packed = msgpack.dumps(msg)
    socket.send(packed)


def listen():
    rospy.init_node("zmq_server", anonymous=True)
    # rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rospy.Subscriber("/joint_states", JointState, callback2)
    rospy.spin()

if __name__ == '__main__':
    listen()
