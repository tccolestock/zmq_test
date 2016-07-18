#!/usr/bin/env python

# uses the turtlesim color to test taking data from ros and pushing it to zmq

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color
from sensor_msgs.msg import JointState
import zmq
import cPickle as pickle
# import mystuff

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


def callback(data):
    print(data.position[1])
    pickled = pickle.dumps(data, -1)
    # print(pickled)
    print("pickling.... \n")
    socket.send(pickled)
    # x = "Hello"
    # pub.publish(x)

def callback2(data):
    d = data.position[1]
    # pickled = pickle.dumps(d, -1)
    print("pickling... \n")
    socket.send(b'%03f' % d)
    print(d)

def listen():
    rospy.init_node("zmq_turtle_server", anonymous=True)
    # rate = rospy.Rate(10) #hz
    # pub = rospy.Publisher("test2", String, queue_size=10)
    rospy.Subscriber("/joint_states", JointState, callback)
    rospy.spin()

# while not rospy.is_shutdown():
    # rate.sleep()

if __name__ == '__main__':
    listen()
