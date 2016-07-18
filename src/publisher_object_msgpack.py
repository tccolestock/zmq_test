#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
from sr_robot_msgs.msg import BiotacAll
from geometry_msgs.msg import Twist
import zmq
import msgpack
from rospy_msgpack import sensor_msgs
from rospy_msgpack import turtlesim
from rospy_msgpack import sr_robot_msgs
from rospy_msgpack import geometry_msgs


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Create encoding objects
sensor_encode = sensor_msgs.Encode()
turtle_encode = turtlesim.Encode()
bio_encode = sr_robot_msgs.Encode()
geo_encode = geometry_msgs.Encode()

def callback(color):
    print("in callback")
    msg = geo_encode.twist(color)
    print(msg)
    packed = msgpack.dumps(msg)
    socket.send(packed)

def callback2(state):
    msg = sensor_encode.joint_state(state)
    print(msg)
    packed = msgpack.dumps(msg)
    socket.send(packed)

def callback3(bio):
    msg = bio_encode.biotac_all(bio)
    print(msg)
    packed = msgpack.dumps(msg)
    socket.send(packed)

def listen():
    rospy.init_node("zmq_server", anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    # rospy.Subscriber("/joint_states", JointState, callback2)
    # rospy.Subscriber("/rh/tactile", BiotacAll, callback3)
    rospy.spin()

if __name__ == '__main__':
    listen()
