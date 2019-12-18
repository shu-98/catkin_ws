#!/usr/bin/env python
# coding:utf-8

## 信号が来たタイミングでサーボ（ロボットの耳）を動かすノード

import rospy
from std_msgs.msg import Int16
import datetime
import sys
import subprocess
import time

import signal
from twisted.internet import task, reactor

INTERVAL = 0.5

# arduino
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)   #　差し直しなどでttyACM0以外の時は適宜変更

#　サーボの初期設定
SERVO_INIT_DEGREE = 90
RIGHT_SERVO_INIT_DEGREE = SERVO_INIT_DEGREE+2    ## 足すと時計回り,引くと反時計回り
LEFT_SERVO_INIT_DEGREE = SERVO_INIT_DEGREE+6
CYCLE_ANGLE = 15

cy_curr_time = 500.0
cy_prev_time = 0.0
cycle_first_flag = 1

def move_servo(data_right, data_left):
    buff = str(data_right) + "r" + str(data_left) + "l"
    ser.write(buff)
    print("%s, %s" % (data_left, data_right))

def input_time():
    t = datetime.datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    return d

def loop():
    move_servo(RIGHT_SERVO_INIT_DEGREE-CYCLE_ANGLE, LEFT_SERVO_INIT_DEGREE+CYCLE_ANGLE)
    time.sleep(0.1)
    move_servo(RIGHT_SERVO_INIT_DEGREE, LEFT_SERVO_INIT_DEGREE)

def loop_start():
    # 実行間隔
    interval = INTERVAL

    # ループに関数を登録して、指定された間隔で実行する
    instance = task.LoopingCall(loop)
    instance.start(interval)

    # twistedのイベントループを開始する
    reactor.run()

    signal.signal(signal.SIGINT, handler)
    signal.pause()

def callback(data):
    global cycle_first_flag
    global cy_prev_time
    global cy_curr_time

    time_sub = cy_curr_time-cy_prev_time

    if cycle_first_flag == 1:
        if time_sub < 0.15 and time_sub > -0.15:
            cycle_first_flag = 0
            loop_start()
        else:
            cy_prev_time = cy_curr_time
            cy_curr_time = input_time()

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping robot's ears...")

def listener():
    rospy.init_node('main_arduino', anonymous=True)

    #cmd_ACへのメッセージを受け取るとcallback1を実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    time.sleep(1.5) # Arduinoの起動時間待機
    move_servo(RIGHT_SERVO_INIT_DEGREE, LEFT_SERVO_INIT_DEGREE)
    listener()
