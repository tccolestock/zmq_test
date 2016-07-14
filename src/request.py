#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def talker():
    rospy.init_node("zmq_request", anonymous=True)
    pub = rospy.Publisher("req_out", Float32, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(500) #hz

    while not rospy.is_shutdown():
        socket.send(b"now")
        msg = socket.recv_string()
        msg = float(msg)
        print(msg)
        # pub.publish(msg)
        rate_handle.sleep()


if __name__ == '__main__':
    talker()
