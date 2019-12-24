#!/usr/bin/env python
# coding:utf-8

## 各ノードに"INTERVAL"秒ごとに信号を送るノード

import signal
from twisted.internet import task, reactor
import datetime
import time

# ROS,message
import rospy
from std_msgs.msg import Int16

INTERVAL = rospy.get_param("interval", 0.5)

## cmd_ACの信号を初期化
pub = rospy.Publisher('cmd_AC', Int16, queue_size=10)

## 現在時間を返す関数
def time_print():
    t = datetime.datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    print "d:", d

## よくわからんけど必要らしい（これとmainのやつで周期的に動作するように出来てるらしい）
def handler(signum, frame):
    print("signal={}".format(signum))

## cmd_ACの信号をpublishする
def send():
    time_print()
    pub.publish(1)

##
if __name__ == "__main__":
    rospy.init_node('cycle', anonymous=True)

    # 実行間隔
    interval = INTERVAL

    # ループに関数を登録して、指定された間隔で実行する
    instance = task.LoopingCall(send)
    instance.start(interval)

    # twistedのイベントループを開始する
    reactor.run()

    signal.signal(signal.SIGINT, handler)
    signal.pause()
