#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import math
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from tf import transformations
from std_srvs.srv import *
import time
from assignment_2_2022.msg import nodeA

# Brings in the SimpleActionClient
import actionlib
import actionlib_msgs
import assignment_2_2022.msg


def msg_callback(info):
 pub = rospy.Publisher('chatter', nodeA, queue_size=10)
 #while not rospy.is_shutdown():
 message=nodeA()
 message.x=info.pose.pose.position.x
 message.y=info.pose.pose.position.y
 message.velx=info.twist.twist.linear.x
 message.vely=info.twist.twist.linear.y
 print(message)
 rate = rospy.Rate(20) # 10hz
 pub.publish(message)
 rate.sleep()
  
  
 


if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('nodeAmsg')
        rospy.Subscriber("/odom", Odometry, msg_callback)
        rospy.spin()
        
       
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
