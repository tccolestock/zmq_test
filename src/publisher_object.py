#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
import zmq
import pickle

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

rospy.init_node("zmq_turtle_server", anonymous=True)
rate = rospy.Rate(1) #hz

def callback(data):
    pickled = pickle.dumps(data)
    print(pickled)
    socket.send_string(pickled)


while not rospy.is_shutdown():
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rate.sleep()
