#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")

rospy.init_node("zmq_turtle_client", anonymous=True)
pub = rospy.Publisher("test_out", Float32, queue_size=10)


while not rospy.is_shutdown():
    message = socket.recv()
    message = float(message)
    print(message)
    # print(message*2)
    # print("in while loop")
    pub.publish(message)
    
