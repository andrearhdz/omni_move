#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():

    valor = int(input("Ingresa el valor de RPM: "))

    if valor > 300 or valor < 50:
        valor = int(input("El valor debe de estar en un rango de entre 50 a 300 RPM: "))

    pub = rospy.Publisher('set_PWM', String, queue_size=10)
    rospy.init_node('pwm', anonymous=True)
    
    pub.publish(valor)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
