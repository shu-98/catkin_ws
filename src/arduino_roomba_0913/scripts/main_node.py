#!/usr/bin/env python
# coding:utf-8

## 信号が来たタイミングでサーボ（ロボットの耳）を動かすノード

import rospy
from std_msgs.msg import Int16
import datetime
import sys
import wiringpi
import subprocess

SERVO1  =  12
SERVO2  =  13

#　サーボの初期設定
SERVO_INIT_DEGREE = 60
CYCLE_ANGLE = 15
zigflag = 0

cy_curr_time = 500.0
cy_prev_time = 0.0
cycle_first_flag = 1

def init_servo(servo1, servo2):
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode( servo1, 2 )
    wiringpi.pinMode( servo2, 2 )
    wiringpi.pwmSetMode(0)
    wiringpi.pwmSetRange(1024)
    wiringpi.pwmSetClock(375)

def move_servo(degree, servo):
    move_deg = int( 81 + 41 / 90.0 * degree )
    wiringpi.pwmWrite( servo, move_deg )

def input_time():
    t = datetime.datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    return d

def serial_connect(data_right, data_left):
    move_servo(data_right, SERVO1)
    move_servo(data_left, SERVO2)
    print("%s, %s" % (data_left, data_right))

def callback(data):
    global zigflag

    global cycle_first_flag
    global cy_prev_time
    global cy_curr_time

    temp_right = SERVO_INIT_DEGREE
    temp_left = SERVO_INIT_DEGREE

    time_sub = cy_curr_time-cy_prev_time

    if cycle_first_flag == 1:
        if time_sub < 0.15 and time_sub > -0.15:
            zipflag = 1
            cycle_first_flag = 0
        else:
            cy_prev_time = cy_curr_time
            cy_curr_time = input_time()
            return
    else:
        if zigflag == 0:
            temp_right += CYCLE_ANGLE
            temp_left += -CYCLE_ANGLE
            zigflag = 1
        elif zigflag == 1:
            temp_right += 0
            temp_left += 0
            zigflag = 0

    serial_connect(temp_right, temp_left)

def shutdown():
    # Always stop the Roomba when shutting down the node.
    wiringpi.pwmWrite( SERVO1, 0 )
    wiringpi.pwmWrite( SERVO2, 0 )
    subprocess.call("gpio -g mode %s IN" % (SERVO1), shell=True)
    subprocess.call("gpio -g mode %s IN" % (SERVO2), shell=True)
    rospy.loginfo("Stopping robot's ears...")

def listener():
    rospy.init_node('nodemain', anonymous=True)

    #cmd_ACへのメッセージを受け取るとcallback1を実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    init_servo(SERVO1, SERVO2)
    move_servo(SERVO_INIT_DEGREE, SERVO1)
    move_servo(SERVO_INIT_DEGREE, SERVO2)
    listener()
