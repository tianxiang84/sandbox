#!/usr/bin/env python

import rospy
import tf

# start a ros node
rospy.init_node('tf_broadcaster')

# initialize a tf broadcaster
br = tf.TransformBroadcaster()
rate = rospy.Rate(2)

while True:
  position = (1,0,0)
  quaternion = (0,0,0,1)
  time = rospy.Time.now()
  frame_1 = 'frame_1'
  frame_2 = 'frame_2'
  br.sendTransform(position, quaternion, time, frame_1, frame_2)
  rate.sleep()

  position = (0,0,-1)
  quaternion = (0,0.707,0,0.707)
  time = rospy.Time.now()
  frame_2 = 'frame_2'
  frame_3 = 'frame_3'
  br.sendTransform(position, quaternion, time, frame_2, frame_3)
  rate.sleep()


