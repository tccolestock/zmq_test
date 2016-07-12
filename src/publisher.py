#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

rospy.init_node("zmq_turtle_server", anonymous=True)
rate = rospy.Rate(1) #hz

def callback(data):
    # data = data
    value = data.r
    # pub.publish(value)
    print("Value: %f" % value)
    socket.send(b"%03d" % value)

# pub = rospy.Publisher("server_pub", UInt8, queue_size=10)

while not rospy.is_shutdown():
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rate.sleep()
