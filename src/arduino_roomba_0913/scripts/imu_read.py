#!/usr/bin/env python
# coding:utf-8

## 各ノードに"INTERVAL"秒ごとに信号を送るノード

import rospy
from std_msgs.msg import String
import serial

ser = serial.Serial('/dev/rfcomm2', 9600)   #　差し直しなどでttyACM0以外の時は適宜変更
pub = rospy.Publisher('imu', String, queue_size=10)
line = ""

##
if __name__ == "__main__":
    rospy.init_node('imu_read', anonymous=True)

    while True:
        line = ""
        try:
            line = ser.readline()
        except KeyboardInterrupt:
            ser.close()
            print("finished imu_read...")
            break
        if line != "":
            print(line.rstrip())
            pub.publish(line)

    # try:
    #     while True:
    #         line = ""
    #         line = ser.readline()
    #         if line != "":
    #             print(line.rstrip())
    #             pub.publish(line)
    # except KeyboardInterrupt:
    #     ser.close()
    #     print("finished imu_read...")
