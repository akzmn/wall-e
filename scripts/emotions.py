#!/usr/bin/python
import roslib; roslib.load_manifest('walle')
import rospy
from std_msgs.msg import String
from std_msgs.msg import Char
from walle.msg import *
import random

def interaction_callback(data):
	global message
	wave = data.wave
	hello = data.hello
	goodbye = data.goodbye
	if wave:
		print "waved!"
		message = random.randint(8, 11)
	if hello:
		print "hello!"
		message = 13
	if goodbye:
		print "goodbye"
		message = 14
	if not goodbye and not hello and not wave:
		print "none work"
		message = 0
	print message


def comms_callback(data):
	if "close" in data:
		message = 6


def publisher():
	global message
	rospy.init_node("interaction_node", anonymous = True)
	rospy.Subscriber("/detected_gestures", gestures, interaction_callback)
	rospy.Subscriber("/drive_comms", String, comms_callback)
	pub = rospy.Publisher('/emotion', Char)
	r = rospy.Rate(20)
	while not rospy.is_shutdown():
		if message != 0:
			msg = message
			pub.publish(msg)
		r.sleep()
       
if __name__ == "__main__":
	message = 0
   	publisher()