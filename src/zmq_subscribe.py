#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import zmq
from turtlesim.msg import Color

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")

rospy.init_node("zmq_turtle_client", anonymous=True)
pub = rospy.Publisher("test_out", Color, queue_size=10)


while not rospy.is_shutdown():
    message = socket.recv_multipart()
    # message = float(message)
    print(len(message))
    color = Color()
    color.r = int(message[0])
    color.g = int(message[1])
    color.b = int(message[2])
    # r = message[0]
    # g = message[1]
    # b = message[2]



    # print(message*2)
    # print("in while loop")
    pub.publish(color)
