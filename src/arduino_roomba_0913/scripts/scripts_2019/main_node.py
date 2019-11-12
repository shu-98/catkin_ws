#!/usr/bin/env python
# coding:utf-8

## GPIOピン(18,19)に繋げればそのあま使える？

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import time
import datetime
import sys

## GPIO
# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# サーボモータに接続したGPIO端子番号を指定
servo_pin1  =  18
servo_pin2  =  12
# サーボモータを動かす角度を指定する
set_degree = 0
wiringpi.wiringPiSetupGpio()
# ハードウェアPWMで出力する
wiringpi.pinMode( servo_pin1, 2 )    # 1=INPUT, 2=OUTPUT (?)
wiringpi.pinMode( servo_pin2, 2 )
# サーボモータに合わせたPWM波形の設定
wiringpi.pwmSetMode(0)
wiringpi.pwmSetRange(1024)
wiringpi.pwmSetClock(375)

# 角度から送り出すPWMのパルス幅を算出する
move_deg = int( 81 + 41 / 90 * set_degree )
# サーボモータにPWMを送り、サーボモータを動かす
wiringpi.pwmWrite( servo_pin1, move_deg )
wiringpi.pwmWrite( servo_pin2, move_deg )
## GPIO

#　サーボの初期設定
RIGHT_INIT = -10
LEFT_INIT = -7
JOY_ANGLE = 15
CYCLE_ANGLE = 10

# DEFINE
SPEED_AN = JOY_ANGLE
TURN_AN = JOY_ANGLE
CYCLE_AN = CYCLE_ANGLE

LEFT_MAX = LEFT_INIT + 90 + JOY_ANGLE + CYCLE_ANGLE
LEFT_MIN = LEFT_INIT + 90 - JOY_ANGLE - CYCLE_ANGLE
RIGHT_MAX = RIGHT_INIT + 90 + JOY_ANGLE + CYCLE_ANGLE
RIGHT_MIN = RIGHT_INIT + 90 - JOY_ANGLE - CYCLE_ANGLE

zigflag = 0

#　平行になる値
temp_right = RIGHT_INIT + 90
temp_left = LEFT_INIT + 90

angle_right = 0
angle_left = 0
cycle_flag = 0

first_flag = 0
curr_time = 0.0
prev_time = 0.0
cy_curr_time = 500.0
cy_prev_time = 0.0

cycle_first_flag = 0

#　ログのための保存変数
joy_x = 0.0
joy_z = 0.0
program_start_time = 0.0

prev_right = temp_right
prev_left = temp_left

print "init-option"
print "RIGHT_MAX = %d, RIGHT_MIN = %d" % (RIGHT_MAX, RIGHT_MIN)
print "LEFT_MAX  = %d, LEFT_MIN  = %d" % (LEFT_MAX, LEFT_MIN)
print ""

def input_time():
    t = datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    return d

def serial_connect(data_right, data_left):
    global first_flag
    global curr_time
    global prev_time
    global cycle_flag

    if cycle_flag == 1 or first_flag == 0 or (curr_time - prev_time) >= 0.025:
        print("%s, %s" % (data_left, data_right))
        prev_time = input_time()
        # 角度から送り出すPWMのパルス幅を算出する
        move_deg1 = int( 81 + 41 / 90 * data_right )
        move_deg2 = int( 81 + 41 / 90 * data_left )
        # サーボモータにPWMを送り、サーボモータを動かす
        wiringpi.pwmWrite( servo_pin1, move_deg1 )
        wiringpi.pwmWrite( servo_pin2, move_deg2 )
        ## GPIO
        first_flag = 1
        cycle_flag = 0

def callback(data):
    global zigflag
    global cycle_flag

    global temp_right
    global temp_left
    global prev_right
    global prev_left

    global cycle_first_flag
    global cy_prev_time
    global cy_curr_time

    time_sub = cy_curr_time-cy_prev_time

    if cycle_first_flag == 0:
        if time_sub < 0.15 and time_sub > -0.15:
            zipflag = 1
            cycle_flag = 1
            cycle_first_flag = 1
        else:
            pass
    else:
        if zigflag == 0:
            zigflag = 1
        elif zigflag == 1:
            zigflag = 0
        cycle_flag = 1

    temp_right = prev_right
    temp_left = prev_left
    cy_prev_time = cy_curr_time
    cy_curr_time = input_time()

    #　閾値設定
    if temp_right < RIGHT_MIN:
        temp_right = RIGHT_MIN
    elif temp_right > RIGHT_MAX:
        temp_right = RIGHT_MAX
    if temp_left > LEFT_MAX:
        temp_left = LEFT_MAX
    elif temp_left < LEFT_MIN:
        temp_left = LEFT_MIN

    prev_right = temp_right
    prev_left = temp_left

    if cycle_first_flag == 1:
        if zigflag == 0:
            temp_right += CYCLE_AN
            temp_left += -CYCLE_AN    #　左右対称
        elif zigflag == 1:
            temp_right += 0
            temp_left += 0    #　左右対称

    curr_time = input_time()
    serial_connect(temp_right, temp_left)
    temp_right = RIGHT_INIT + 90
    temp_left = LEFT_INIT + 90

def shutdown():
    # Always stop the Roomba when shutting down the node.
    wiringpi.pwmWrite( servo_pin1, 0 )
    wiringpi.pwmWrite( servo_pin2, 0 )
    rospy.loginfo("Stopping robot's ears...")

def listener():
    rospy.init_node('nodemain', anonymous=True)

    #cmd_ACへのメッセージを受け取るとcallback1を実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    program_start_time = input_time()
    listener()
