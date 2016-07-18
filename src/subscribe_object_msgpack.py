#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import zmq
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
import time
import msgpack
from rospy_msgpack import sensor_msgs
from rospy_msgpack import turtlesim

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")

# Create decoding objects
sensor_decode = sensor_msgs.Decode()
turtle_decode = turtlesim.Decode()

def talker():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("test_color", Color, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500) #hz

    while not rospy.is_shutdown():
        rec = socket.recv()
        msg = msgpack.loads(rec)
        color = Color()
        print(dir(decode))
        color = turtle_decode.color(msg, color)
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

if __name__ == '__main__':
    try:
        # talker()
        talker2()
    except rospy.ROSInterruptException:
        pass
