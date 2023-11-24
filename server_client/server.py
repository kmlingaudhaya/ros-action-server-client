#!/usr/bin/env python3

import rospy
import actionlib
from test_1.msg import TestAction, TestGoal, TestResult

class TestServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('test_1', TestAction, self.execute_callback, False)
        self.server.start()
        rospy.loginfo("Server is ready to receive goals")

    def execute_callback(self, goal):
        # Assuming the goal is an integer, you can access it as goal.order
        input_number = goal.order
        rospy.loginfo("Received goal with order: %d" % input_number)

        # Your processing logic here to generate a sequence based on the input
        result_sequence = self.generate_sequence(input_number)

        result = TestResult()
        result.sequence = result_sequence
        rospy.loginfo("Returning sequence: %s" % str(result_sequence))

        self.server.set_succeeded(result)

    def generate_sequence(self, n):
        # Your sequence generation logic here, this is just an example
        return [i for i in range(n)]

if __name__ == '__main__':
    rospy.init_node('test_server')
    server = TestServer()
    rospy.spin()
