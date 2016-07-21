#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import zmq
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
# from sr_robot_msgs.msg import BiotacAll
from geometry_msgs.msg import Twist, Polygon
import time
import msgpack
from rospy_msgpack import turtlesim_msgpack
from rospy_msgpack import sensor_msgpack
from rospy_msgpack import sr_robot_msgpack
from rospy_msgpack import geometry_msgpack
import StringIO

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")

# Create decoding objects
turtle_decode = turtlesim_msgpack.Decode()
sensor_decode = sensor_msgpack.Decode()
bio_decode = sr_robot_msgpack.Decode()
geo_decode = geometry_msgpack.Decode()

def talker():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("test_velo", Twist, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500) #hz

    while not rospy.is_shutdown():
        rec = socket.recv()
        msg = msgpack.loads(rec)
        color = Twist()
        # print(dir(decode))
        color = geo_decode.twist(msg, color)
        # color.deserialize()
        print(color)
        pub.publish(color)

def talker2():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("test_js", JointState, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500) #hz
    while not rospy.is_shutdown():
        rec = socket.recv()
        msg = msgpack.loads(rec)
        state = JointState()
        state = sensor_decode.joint_state(msg, state)
        print(state)
        pub.publish(state)

def talker3():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("test_bio", BiotacAll, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500) #hz
    while not rospy.is_shutdown():
        rec = socket.recv()
        msg = msgpack.loads(rec)
        bio = BiotacAll()
        state = bio_decode.biotac_all(msg, bio)
        print(bio)
        pub.publish(bio)

def talker4():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("test_out", Polygon, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500) #hz
    while not rospy.is_shutdown():
        rec = socket.recv()
        msg = msgpack.loads(rec)
        poly = Polygon()
        state = geo_decode.polygon(msg, poly)
        print(poly)
        pub.publish(poly)

if __name__ == '__main__':
    try:
        # talker()
        talker4()
    except rospy.ROSInterruptException:
        pass
