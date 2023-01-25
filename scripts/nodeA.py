#! /usr/bin/env python


from __future__ import print_function
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

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.


def new_position():
 global client
 
 
 client.wait_for_server()
 goal=PoseStamped()
 xpos=input('\nEnter posx: ')
 ypos=input('\nEnter posy: ')
 goal.pose.position.x=int(xpos)
 goal.pose.position.y=int(ypos)
 goal = assignment_2_2022.msg.PlanningGoal(goal)
 client.send_goal(goal)
 rospy.sleep(2)



 user_select()

def cancel_sim():
 #client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
 client.cancel_goal()
 print("goal cancelled: going back to user select...")
 user_select()

def user_select():
 
 op=input("choose action: ")
 

 if(op=="1"):
    new_position()
 elif(op=="2"):
    cancel_sim()

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        print("1: define position")
        print("2: cancel")
        rospy.init_node('nodeAclient')
        
        client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
        
        user_select()
      
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
