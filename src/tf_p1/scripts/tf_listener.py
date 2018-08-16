#!/usr/bin/env python

import rospy
import tf

# start a ros node
rospy.init_node('tf_listener')

# initialize a tf listener
listener = tf.TransformListener()

#rospy.loginfo('into the code?')
base = '/frame_3'
child = '/frame_1'
while not rospy.is_shutdown():
  try:
    #rospy.loginfo('listening')
    (position, orientation) = listener.lookupTransform(base, child, rospy.Time(0))
    #rospy.loginfo('{}:{}'.format(position,orientation))
  except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    #rospy.loginfo('Exception...')
    continue
  
  print('position: {}\norientation: {}'.format(position, orientation))
