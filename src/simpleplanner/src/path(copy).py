#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pi

def move(speed, distance, isForward):
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/vrep/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    #speed = input("Input your speed:")
    #speed = 0.1
    #distance = input("Type your distance:")
    #distance = 0.1
    #isForward = input("Foward?: ")#True or False
    #isForward = 1

    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0.1
    vel_msg.angular.y = 0.1
    vel_msg.angular.z = 0.1

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        #Stop code on finish
        break

if __name__ == '__main__':
    try:
        #Testing our function
        move(0.1, 0.1, 1)
        print('Go home')
        #Stop process (sigterm -15)
        exit()
    except rospy.ROSInterruptException: pass
