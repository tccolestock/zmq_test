#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String, Float32, UInt8
from sensor_msgs.msg import JointState
import baxter_interface

rospy.init_node("sh2bax_move_elbow", anonymous=True)
limb = baxter_interface.Limb('left')
angles = limb.joint_angles()
angles['left_e1']=0.0

wave_1 = {'left_s0': -0.459, 'left_s1': -0.202, 'left_e0': 1.807, 'left_e1': 1.714, 'left_w0': -0.906, 'left_w1': -1.545, 'left_w2': -0.276}

def callback(data):
    d = data
    index = d.name.index('rh_FFJ2')
    finger_pos = d.position[index]
    target = {'left_e1': finger_pos}
    limb.move_to_joint_positions(target)


def listen():
    rospy.Subscriber("/test_out", JointState , callback)
    pub = rospy.Publisher("topic_name", Message_Type, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listen()
