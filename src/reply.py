#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import time
import zmq
from sensor_msgs.msg import JointState

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def callback(data):
    d = data.position[1]
    message = socket.recv()
    if message == "now":
        socket.send_string(b"%03f" % d)
        print(d)
        message = ""

def listen():
    rospy.init_node("zmq_reply", anonymous=True)
    # message = socket.recv()
    rospy.Subscriber("/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listen()
