#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import Joy
import sys

# CSVファイルに書き込み
import csv # CSVファイルを扱うためのモジュールのインポート
from datetime import datetime
filename = "log/log_%s.csv" % (datetime.now().strftime('%Y%m%d-%H%M%S'))
writecsv = csv.writer(file(filename, 'w'), lineterminator='\n') # 書き込みファイルの設定
writecsv.writerow(['datetime', 'second', 'joy_x', 'joy_z', 'tempo', 'bgm_start'])

joy_x = 0.0
joy_z = 0.0
program_start_time = 0.0

def input_time():
    t = datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    return d

def write_joy(data):
    global joy_x
    global joy_z

    joy_x = data.axes[1]
    joy_z = data.axes[0]

    date = datetime.now()
    second = input_time() - program_start_time
    writecsv.writerow([date, str(second), str(joy_x), str(joy_z), '0', '0'])

def write_rhythm(data):
    date = datetime.now()
    second = input_time() - program_start_time
    writecsv.writerow([date, str(second), str(joy_x), str(joy_z), '1', '0'])

def write_music(data):
    date = datetime.now()
    second = input_time() - program_start_time
    writecsv.writerow([date, str(second), str(joy_x), str(joy_z), '0', '1'])

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping writing log...")

def listener():
    rospy.init_node('nodemain', anonymous=True)

    #cmd_JCへのメッセージを受け取るとwrite_joyを実行
    rospy.Subscriber('joy', Joy, write_joy)
    #cmd_ACへのメッセージを受け取るとwrite_rhythm1を実行
    rospy.Subscriber('cmd_AC', Int16, write_rhythm)
    #musicノードから
    rospy.Subscriber('cmd_MC', Int16, write_music)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    program_start_time = input_time()
    listener()
