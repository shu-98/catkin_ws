#!/usr/bin/env python
# coding:utf-8

## 信号が来たタイミングでサーボ（ロボットの耳）を動かすノード

import rospy
from std_msgs.msg import Int16
import datetime
import sys
import subprocess
import time

# arduino
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)   #　差し直しなどでttyACM0以外の時は適宜変更

#　サーボの初期設定
SERVO_INIT_DEGREE = 90
RIGHT_SERVO_INIT_DEGREE = SERVO_INIT_DEGREE+7    ## 足すと時計回り,引くと反時計回り
LEFT_SERVO_INIT_DEGREE = SERVO_INIT_DEGREE-3
CYCLE_ANGLE = 15
zigflag = 0

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

def callback(data):
    global zigflag

    global cycle_first_flag
    global cy_prev_time
    global cy_curr_time

    temp_right = RIGHT_SERVO_INIT_DEGREE
    temp_left = LEFT_SERVO_INIT_DEGREE

    time_sub = cy_curr_time-cy_prev_time

    if cycle_first_flag == 1:
        if time_sub < 0.15 and time_sub > -0.15:
            zipflag = 1
            cycle_first_flag = 0
        else:
            cy_prev_time = cy_curr_time
            cy_curr_time = input_time()
            return
    if zigflag == 0:
        temp_right -= CYCLE_ANGLE
        temp_left += CYCLE_ANGLE
        zigflag = 1
    elif zigflag == 1:
        ## なにもしない
        zigflag = 0

    move_servo(temp_right, temp_left)

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
