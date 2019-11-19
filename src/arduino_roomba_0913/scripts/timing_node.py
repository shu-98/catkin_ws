#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
import threading
import time
import datetime

#tempo_num = 20*4+10
#tempo_num = 384
tempo_num = 384*2
tempo = tempo_num

pub = rospy.Publisher('cmd_M', Int16, queue_size=10)

def callback(data):
    global tempo

    rospy.loginfo(tempo)
    if tempo >= tempo_num:
        pub.publish(1)
        tempo = 1
    else:
        tempo += 1

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the Music...")

def listener():
    rospy.loginfo("listener()")
    #cmd_JCへのメッセージを受け取るとdecide_angleを実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('timing', anonymous=True)
    time.sleep(2)
    listener()
