#!/usr/bin/env python
import rospy
import math
from assignment_2_2022.msg import nodeA
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped


euc_dist=0

def callback(msg):
#while not rospy.is_shutdown():
    pxd=rospy.get_param("/des_pos_x")
    pyd=rospy.get_param("/des_pos_y")
    px=msg.x
    py=msg.y
    velx=msg.velx
    vely=msg.vely
    euc_dist=math.sqrt(((pxd-px)**2)+((pyd-py)**2))
    print("Distance:",euc_dist, end=" ")
    print("velx:",velx, end=" ")
    print("vely:",vely)
    

if __name__ == '__main__':
    rospy.init_node('nodeC')
    rospy.Subscriber("chatter", nodeA, callback)
    rospy.spin()

