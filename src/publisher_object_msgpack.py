#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
# from sr_robot_msgs.msg import BiotacAll
from geometry_msgs.msg import Twist, Polygon, PoseArray
import zmq
import msgpack
from rospy_msgpack import sensor_msgpack
from rospy_msgpack import turtlesim_msgpack
from rospy_msgpack import sr_robot_msgpack
from rospy_msgpack import geometry_msgpack
import StringIO


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Create encoding objects
sensor_encode = sensor_msgpack.Encode()
turtle_encode = turtlesim_msgpack.Encode()
bio_encode = sr_robot_msgpack.Encode()
geo_encode = geometry_msgpack.Encode()

stio_obj = StringIO.StringIO()

def callback(color):
    print("in callback")
    msg = geo_encode.twist(color)
    # color.serialize(stio_obj)
    print(msg)
    # print(st)
    packed = msgpack.dumps(msg)
    # packed = msgpack.dumps(stio_obj.getvalue())
    socket.send(packed)
    # socket.send(stio_obj.getvalue())

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

def callback4(poly):
    msg = geo_encode.pose_array(poly)
    print(msg)
    packed = msgpack.dumps(msg)
    socket.send(packed)

def listen():
    rospy.init_node("zmq_server", anonymous=True)
    # rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    # rospy.Subscriber("/joint_states", JointState, callback2)
    # rospy.Subscriber("/rh/tactile", BiotacAll, callback3)
    rospy.Subscriber("/test_posearray", PoseArray, callback4)
    rospy.spin()

if __name__ == '__main__':
    listen()
