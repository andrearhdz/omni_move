#!/usr/bin/env python3
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   n         .


s : turn left
f : turn right

anything else : stop

e/d : increase/decrease max speeds by 10%


CTRL-C to quit
"""

moveBindings = {
	'i':(1,0,0,0),
	'o':(1,1,0,0),
	'u':(1,-1,0,0),
	'l':(0,1,0,0),
	'j':(0,-1,0,0),
	'k':(-1,0,0,0),
	'.':(-1,1,0,0),
	'n':(-1,-1,0,0),
	's':(0,0,0,-1),
	'f':(0,0,0,1),
}

speedBindings={
	'e':(1.1,1.1),
	'd':(.9,.9),
}

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def vels(speed,turn):
	return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('teleop_twist_keyboard')

	speed = rospy.get_param("~speed", 0.2)
	turn = rospy.get_param("~turn", 1.0)
	x = 0
	y = 0
	z = 0
	th = 0
	status = 0

	try:
		print (msg)
		print (vels(speed,turn))
		while(1):
			key = getKey()
			if key in moveBindings.keys():
				x = moveBindings[key][0]
				y = moveBindings[key][1]
				z = moveBindings[key][2]
				th = moveBindings[key][3]
			elif key in speedBindings.keys():
				speed = speed * speedBindings[key][0]
				turn = turn * speedBindings[key][1]

				print (vels(speed,turn))
				if (status == 14):
					print (msg)
				status = (status + 1) % 15
			else:
				x = 0
				y = 0
				z = 0
				th = 0
				if (key == '\x03'):
					break

			twist = Twist()
			twist.linear.x = x*speed; twist.linear.y = y*speed; twist.linear.z = z*speed;
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
			pub.publish(twist)

	except:
		print ("e")

	finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		pub.publish(twist)
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

