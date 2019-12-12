#!/usr/bin/env python
# coding:utf-8

## 各ノードに"INTERVAL"秒ごとに信号を送るノード

import datetime
import time
import rospy
from std_msgs.msg import String
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)   #　差し直しなどでttyACM0以外の時は適宜変更
pub = rospy.Publisher('imu', String, queue_size=10)
line = ""

##
if __name__ == "__main__":
    rospy.init_node('imu_read', anonymous=True)

    while True:
        line = ""
        if line=ser.readline() != "":
            print(str)
            pub.publish(str)
