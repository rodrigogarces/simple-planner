#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move(velocity_publisher, speed, distance, isForward):
    # Starts a new node
    vel_msg = Twist()
    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

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
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)

def rotate(velocity_publisher, speed, angle, clockwise):
    #Starts a new node
    vel_msg = Twist()

    #Converting from angles to radians
    angular_speed = speed*PI/180
    relative_angle = angle*PI/180

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)	


if __name__ == '__main__':
    try:
        #Testing our function
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/vrep/cmd_vel', Twist, queue_size=10)
	arq = open("coordenadas.txt", "r");
	arq.readline()
	for line in arq:
	   pos = [int(i) for i in line.split() if i.isdigit()]
	   print(pos)
	   move(velocity_publisher, pos[0], pos[1], pos[2])
	   print("Moveu...")
	   rotate(velocity_publisher, pos[3], pos[4], pos[5])
	   print("Rodou...")
	#move()
    except rospy.ROSInterruptException: pass
