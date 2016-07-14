#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import zmq
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
import cPickle as pickle
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')
print("established socket")


def establish():
    rospy.init_node("zmq_turtle_client", anonymous=True)
    pub = rospy.Publisher("test_out", JointState, queue_size=10)
    pub2 = rospy.Publisher("finger", Float32, queue_size=10)
    time.sleep(2)
    # rate_handle = rospy.Rate(500) #hz

    # while not rospy.is_shutdown():
def read():
    message = socket.recv()
    print("received")
    data = pickle.loads(message)
    print("unpickled")
    index = data.name.index('rh_FFJ2')
    angle = data.position[index]
    print(angle)
    # pub.publish(data)
    # pub2.publish(angle)
    # rate_handle.sleep()
    broadcast(data,angle)
    rospy.spin()

def broadcast(data1, data2):
    pub.publish(data1)
    pub2.publish(data2)
    print("published")

if __name__ == '__main__':
    try:
        establish()
    except rospy.ROSInterruptException:
        pass
