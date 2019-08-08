#!/usr/bin/env python
# coding:utf-8

# thread processing
from twisted.internet import task, reactor
import threading
import datetime
import time

# ROS,message
import rospy
from std_msgs.msg import Int16

pub = rospy.Publisher('cmd_AC', Int16, queue_size=10)

prev_time = 0.0
curr_time = 0.0
time_sub = 0.0

def time_print():
    t = datetime.datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    print "d:", d

def send():
    time_print()
    pub.publish(1)
    time.sleep(0.1)
    pub.publish(1)

if __name__ == "__main__":
    rospy.init_node('nodeA', anonymous=True)

    # 実行間隔
    interval = 0.5

    # ループに関数を登録して、指定された間隔で実行する
    instance = task.LoopingCall(send)
    instance.start(interval)

    # twistedのイベントループを開始する
    reactor.run()
