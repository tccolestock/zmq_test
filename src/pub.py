#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
import time

rospy.init_node("pub_test", anonymous=True)
pub = rospy.Publisher("test3", String, queue_size=10)
time.sleep(2)

def main():
    x = "hello"
    pub.publish(x)

if __name__ == '__main__':
    main()
    rospy.spin()
