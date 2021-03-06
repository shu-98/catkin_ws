#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import sys

# CSVファイルに書き込み
import csv # CSVファイルを扱うためのモジュールのインポート
from datetime import datetime

## 書き込みファイルの設定
filename = "/home/sou/catkin_ws/src/arduino_roomba_0913/scripts/log/log_%s.csv" % (datetime.now().strftime('%Y%m%d-%H%M%S'))
writecsv = csv.writer(file(filename, 'w'), lineterminator='\n')
writecsv.writerow(['datetime', 'second', 'joy_x', 'joy_z', 'tempo', 'bgm_start', 'accx', 'accy', 'accz', 'gyrox', 'gyroy', 'gyroz', 'magx', 'magy', 'magz', 'tempMPU9250'])

joy_x = 0.0 ## ジョイスティックの入力を格納する
joy_z = 0.0 ## ジョイスティックの入力を格納する

roll = ""
yaw = ""
pitch = ""
imu_data = [""]*10

program_start_time = 0.0

## 現在時間を返す関数
def input_time():
    t = datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    return d

## ジョイスティックの入力をログに書き込み
def write_joy(data):
    global joy_x
    global joy_z

    joy_x = data.axes[1]    ## data.axes[1]に３Dスティックの上下入力
    joy_z = data.axes[0]    ## data.axes[1]に３Dスティックの左右入力

    date = datetime.now()
    second = input_time() - program_start_time
    row = [date, str(second), str(joy_x), str(joy_z), '0', '0']
    row.extend(imu_data)
    writecsv.writerow(row)

## リズムが来たタイミングでログに書き込み
def write_rhythm(data):
    date = datetime.now()
    second = input_time() - program_start_time
    row = [date, str(second), str(joy_x), str(joy_z), '1', '0']
    row.extend(imu_data)
    writecsv.writerow(row)

## 音楽が再生したタイミングでログに書き込み
def write_music(data):
    date = datetime.now()
    second = input_time() - program_start_time
    row = [date, str(second), str(joy_x), str(joy_z), '0', '1']
    row.extend(imu_data)
    writecsv.writerow(row)

def write_imu(data):
    global imu_data

    temp = str(data).replace("\"", "").replace("data: ", "").replace("\\r\\n", "")
    imu_data = temp.split(",")
    date = datetime.now()
    second = input_time() - program_start_time
    row = [date, str(second), str(joy_x), str(joy_z), '0', '0']
    row.extend(imu_data)
    writecsv.writerow(row)

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping writing log...")

def listener():
    rospy.init_node('write_log', anonymous=True)

    ## joyへのメッセージを受け取るとwrite_joyを実行
    rospy.Subscriber('joy', Joy, write_joy)
    ## cmd_ACへのメッセージを受け取るとwrite_rhythmを実行
    rospy.Subscriber('cmd_AC', Int16, write_rhythm)
    ## cmd_MCへのメッセージを受け取るとwrite_musicを実行
    rospy.Subscriber('cmd_MC', Int16, write_music)
    ## cmd_MCへのメッセージを受け取るとwrite_musicを実行
    rospy.Subscriber('imu', String, write_imu)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    program_start_time = input_time()
    listener()
