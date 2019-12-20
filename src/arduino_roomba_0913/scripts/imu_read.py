#!/usr/bin/env python
# coding:utf-8

## IMUからのデータをBLEシリアル通信で受け取り,Write_logにデータを送信する

import rospy
from std_msgs.msg import String
import serial

ser = serial.Serial('/dev/rfcomm2', 9600)   #　差し直しなどでttyACM0以外の時は適宜変更
pub = rospy.Publisher('imu', String, queue_size=10)
line = ""

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
