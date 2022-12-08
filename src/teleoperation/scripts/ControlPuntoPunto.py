#!/usr/bin/env python

import math
from math import sin, cos, pi, sqrt
import string
from std_msgs.msg import String, Float32, Float32MultiArray
import numpy as np

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

#robot = [posicion x, posicion y, theta]
robot = [0,0,0]

def getInfo(data):
    global robot
    robot[0]=data.position.x
    robot[1] = data.position.y
    robot[2] = data.position.z



def calcError(targetX, targetY):
    global robot
    etheta = np.arctan2(targetX, targetY)-robot[2]
    ed = sqrt((targetX - robot[0])**2 + (targetY - robot[1])**2)
    posNeg=1
    if (targetX-robot[0] and targetY - robot[1]):
        posNeg=-1
    return etheta, ed, posNeg

def controlPID(etheta, ed, posNeg):
    posNeg=1
    Kv=1*posNeg
    Kw=1*posNeg
    v = Kv * ed
    w = Kw * etheta
    return v,w


def main():
    ed =100 
    etheta =100
    rospy.init_node('error_calculator')
    r = rospy.Rate(2.0)
    error_pub = rospy.Publisher("errores", String, queue_size=50)
    robot_sub = rospy.Subscriber("posicion", Pose, getInfo)
    vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size = 50)
    targetX = int(input("Ingrese la x deseada: "))
    targetY = int(input("Ingrese la y deseada: "))
    while(ed>0.2 or ed < -0.2):
        etheta, ed, posNeg = calcError(targetX, targetY)
        if (etheta >=2*pi):
            etheta -= 2*pi
        if (etheta <=-2*pi):
            etheta += 2*pi  
        #errores = [etheta, ed]
        errorTheta = "etheta: " + str(etheta)
        errorDist = "ed: " + str(ed)
        error_pub.publish(errorTheta)
        error_pub.publish(errorDist)
        v, w =controlPID(etheta, ed, posNeg)
        if (etheta <0.1 and etheta > -0.1):
            w=0.0
        velocity = Twist()
        velocity.linear.x = v/5
        velocity.angular.z = 0
        vel_pub.publish(velocity)
        r.sleep()
        velocity.linear.x = 0
        velocity.angular.z = w/5
        vel_pub.publish(velocity)
        r.sleep()
    velocity = Twist()
    velocity.linear.x = 0
    velocity.angular.z = 0
    vel_pub.publish(velocity)

main()