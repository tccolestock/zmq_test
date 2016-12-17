#!/usr/bin/env python

from __future__ import division

import time
import cPickle as pickle

import rospy
import zmq

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
from sensor_msgs.msg import JointState


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")


def talker():
    rospy.init_node("zmq_turtle_client", anonymous=True)
    pub = rospy.Publisher("test_out", JointState, queue_size=10)
    pub2 = rospy.Publisher("finger", Float32, queue_size=10)
    time.sleep(2)
    rate_handle = rospy.Rate(500)  # hz

    while not rospy.is_shutdown():
        message = socket.recv()
        print("received")
        data = pickle.loads(message)
        print("unpickled")
        index = data.name.index('rh_FFJ2')
        angle = data.position[index]
        print(angle)
        pub.publish(data)
        pub2.publish(angle)
        print("published")
        rate_handle.sleep()


def talker2():
    rospy.init_node("zmq_client", anonymous=True)
    pub = rospy.Publisher("finger", Float32, queue_size=10)
    time.sleep(2)
    rate_handle = rospy.Rate(500)  # hz

    while not rospy.is_shutdown():
        msg = socket.recv()
        msg = float(msg)
        # data = pickle.loads(msg)
        print(msg)
        pub.publish(msg)
        rate_handle.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
