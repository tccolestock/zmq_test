#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

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
    # value = []
    # value.append(data.r)
    # value.append(data.g)
    # value.append(data.b)
    # pub.publish(value)
    # print(value)
    # socket.send(b"%03d" % value)
    print(size(data))
    socket.send_multipart([b"%03d" % data.r, b"%03d" % data.g, b"%03d" % data.b])

# pub = rospy.Publisher("server_pub", UInt8, queue_size=10)

while not rospy.is_shutdown():
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    rate.sleep()
