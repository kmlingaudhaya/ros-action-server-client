#!/usr/bin/env python3

import rospy
import actionlib
from test_1.msg import TestAction, TestGoal

def client():
    # Initialize the ROS node
    rospy.init_node('test_client')

    # Create an action client
    client = actionlib.SimpleActionClient('test_1', TestAction)

    # Wait for the action server to start
    rospy.loginfo("Waiting for action server to start...")
    client.wait_for_server()

    # Create a goal
    goal = TestGoal()
    goal.order = 5  # Replace 5 with your desired integer input

    rospy.loginfo("Sending goal with order: %d", goal.order)

    # Send the goal to the action server
    client.send_goal(goal)

    # Wait for the result
    client.wait_for_result()

    # Process the result
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        result = client.get_result()
        rospy.loginfo("Received sequence: %s" % str(result.sequence))
    else:
        rospy.logerr("Action did not succeed. Current state: %s" % client.get_goal_status_text())

if __name__ == '__main__':
    client()
