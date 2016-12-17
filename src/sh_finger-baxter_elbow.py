#!/usr/bin/env python

""" Not really sure what was happening here. Seems like part
 of the 'pupeteering' that was done between the Shadow Hand
 and the Baxter elbow joint. There should be a more robust
 script somewhere... """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "0.1.0"

import rospy
import baxter_interface

from std_msgs.msg import String, Float32, UInt8
from sensor_msgs.msg import JointState

rospy.init_node("sh2bax_move_elbow", anonymous=True)

limb = baxter_interface.Limb('left')
angles = limb.joint_angles()
angles['left_e1'] = 0.0

wave_1 = {'left_s0': -0.459, 'left_s1': -0.202, 'left_e0': 1.807,
          'left_e1': 1.714, 'left_w0': -0.906, 'left_w1': -1.545,
          'left_w2': -0.276}


def callback(data):
    d = data
    index = d.name.index('rh_FFJ2')
    finger_pos = d.position[index]
    target = {'left_e1': finger_pos}
    limb.move_to_joint_positions(target)


def listen():
    rospy.Subscriber("/test_out", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listen()
