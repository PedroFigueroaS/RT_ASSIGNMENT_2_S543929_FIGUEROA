#! /usr/bin/env python3

import rospy

import time
from std_srvs.srv import Empty, EmptyResponse
import assignment_2_2022.msg

ncancelled=0
nreached=0

def serv_callback(req):
    global ncancelled , nreached
    print(f"\nNumber of canceled goal: {ncancelled}\nnumber of reached goal: {nreached}")
    print("-------------------------------------")
  
    return EmptyResponse()


def cllback(msg):
 
 if (msg.status.status==2):
    global ncancelled
    ncancelled=ncancelled+1
 elif (msg.status.status==3):
    global nreached
    nreached=nreached+1


if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('nodeB')
        rospy.Subscriber("/reaching_goal/result",assignment_2_2022.msg.PlanningActionResult,cllback)
        rospy.Service("reach_cancel_ints",Empty,serv_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
