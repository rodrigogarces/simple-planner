#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pi

def move(lx, ly, lz, ax, ay, az, total_time):
    # Starts a new node

    vel_msg = Twist()

    print("Let's move")

    vel_msg.linear.x = lx
    vel_msg.linear.y = ly
    vel_msg.linear.z = lz
    vel_msg.angular.x = ax
    vel_msg.angular.y = ay
    vel_msg.angular.z = az

    delta_time=0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        initial_time = rospy.Time.now().to_sec()

        velocity_publisher.publish(vel_msg)

        #Loop to move the turtle in an specified distance
        while(delta_time < total_time):
            current_time = rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            delta_time = (current_time - initial_time)
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
    print(delta_time)
    rospy.sleep(0.5)

if __name__ == '__main__':
    try:
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/vrep/cmd_vel', Twist, queue_size=10)
        rospy.sleep(1)

        #cheatsheet
        # move(0.1, 0, 0, 0, 0, 0.1, 3)#Ackermann steering
        # move(0, 0.1, 0, 0, 0, 0.1, 3)#curva de centro frontal
        # move(0, 0, 0.1, 0, 0, 0.1, 3)#curva proprio eixo

        # move(0.5, 0, 0, 0, 0, 0, 3.5)#reta
        # move(0, 0, 0, 0, 0, 0, 0.1)#reta

        move(1, 0, 0, 0, 0, 0, 7)#reta
        move(0, 0, 1, 0, 0, 1, .78)#curva proprio eixo
        move(1, 0, 0, 0, 0, 0, 7)#reta
        move(0, 0, 1, 0, 0, 1, .78)#curva proprio eixo
        move(1, 0, 0, 0, 0, 0, 3)#reta
        move(-1, 0, 0, 0, 0, 0, 6)#reta
        move(0.77, 0, 0, 0, 0, 1, 3.5)#Ackermann steering
        move(0, 0, 0, 0, 0, 0.77, .8)#self axis curve
        move(0, -1, 0, 0, 0, 0, 3)#reta


        print('Go home')
        #Stop process (sigterm -15)
        exit()
    except rospy.ROSInterruptException: pass
