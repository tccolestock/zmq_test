#!/usr/bin/env python

""" Simple publisher"""

from __future__ import division
import time

import rospy

from std_msgs.msg import String, Float32, UInt8

rospy.init_node("pub_test", anonymous=True)
pub = rospy.Publisher("test3", String, queue_size=10)
time.sleep(2)
rate_handle = rospy.Rate(10)  # hz


def main():
    x = "hello"
    pub.publish(x)

if __name__ == '__main__':
    while not rospy.is_shutdown():
        main()
        rate_handle.sleep()
