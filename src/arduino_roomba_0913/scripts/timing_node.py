#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
import threading
import time
import datetime

tempo_num = 384*2   ## "Call_Me_Maybe"が384*2回テンポがあるので
tempo = tempo_num

pub = rospy.Publisher('cmd_M', Int16, queue_size=10)    ## cmd_M信号をpublish

def callback(data):
    global tempo

    rospy.loginfo(tempo)
    ## 曲が一周したらmusic_nodeに信号を送る
    if tempo >= tempo_num:
        pub.publish(1)
        tempo = 1
    else:
        tempo += 1

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the Timing Node...")

def listener():
    rospy.loginfo("listener()")
    ## cmd_ACへのメッセージを受け取るとcallbackを実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('timing', anonymous=True)
    time.sleep(2)
    listener()
