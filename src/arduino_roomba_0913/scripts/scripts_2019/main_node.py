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
import pygame.mixer
#import datetime
import sys

## GPIO
# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# サーボモータに接続したGPIO端子番号を指定
servo_pin1  =  18
servo_pin2  =  19
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

# CSVファイルに書き込み
import csv # CSVファイルを扱うためのモジュールのインポート
from datetime import datetime
filename = "/home/roomba/catkin_ws/src/arduino_roomba/scripts/log/log_%s.csv" % (datetime.now().strftime('%Y%m%d-%H%M%S'))
writecsv = csv.writer(file(filename, 'w'), lineterminator='\n') # 書き込みファイルの設定
writecsv.writerow(['datetime', 'second', 'joy_x', 'joy_z', 'tempo', 'bgm_start'])

# arduino
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)   #　差し直しなどでttyACM0以外の時は適宜変更

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

#pub1 = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
zigflag = 0

#　平行になる値
temp_right = RIGHT_INIT + 90
temp_left = LEFT_INIT + 90

angle_right = 0
angle_left = 0
buff = "" #arduinoに送る文字列
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

## acce
acce_left = 0.0
acce_front = 0.0
acce_up = 0.0
## acce

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
        print(data_left + ", " + data_right)
        prev_time = input_time()
        date = datetime.now()
        second = input_time() - program_start_time
        # 角度から送り出すPWMのパルス幅を算出する
        move_deg1 = int( 81 + 41 / 90 * data_right )
        move_deg2 = int( 81 + 41 / 90 * data_left )
        # サーボモータにPWMを送り、サーボモータを動かす
        wiringpi.pwmWrite( servo_pin1, move_deg1 )
        wiringpi.pwmWrite( servo_pin2, move_deg2 )
        ## GPIO
        writecsv.writerow([date, str(second), str(joy_x), str(joy_z), str(cycle_flag), '0'])
        first_flag = 1
        cycle_flag = 0
    #time.sleep(0.1)

#　追加分
def decide_angle(data):
    global temp_right
    global temp_left
    global joy_x
    global joy_z

    temp_right += int(-data.axes[1]*SPEED_AN + data.axes[0]*TURN_AN)
    temp_left += int(data.axes[1]*SPEED_AN + data.axes[0]*TURN_AN)
    joy_x = data.axes[1]
    joy_z = data.axes[0]

    ##　加速度
    acce_left = data.axes[6]
    acce_front = data.axes[7]
    acce_up = data.axes[8]
    ##　加速度

    move()

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
            zigflag = 2
        elif zigflag == 2:
            zigflag = 3
        elif zigflag == 3:
            zigflag = 4
        elif zigflag == 4:
            zigflag = 5
        elif zigflag == 5:
            zigflag = 6
        elif zigflag == 6:
            zigflag = 7
        elif zigflag == 7:
            zigflag = 0
        cycle_flag = 1

    temp_right = prev_right
    temp_left = prev_left
    cy_prev_time = cy_curr_time
    cy_curr_time = input_time()

    move()

def music_log(data):
    date = datetime.now()
    second = input_time() - program_start_time
    writecsv.writerow([date, str(second), str(joy_x), str(joy_z), '0', '1'])

def move():
    global zigflag
    global temp_right
    global temp_left
    global curr_time

    global prev_right
    global prev_left

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
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += -CYCLE_AN    #　左右対称
        elif zigflag == 1:
            temp_right += 0
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += 0    #　左右対称
        elif zigflag == 2:
            temp_right += CYCLE_AN
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += -CYCLE_AN    #　左右対称
        elif zigflag == 3:
            temp_right += 0
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += 0    #　左右対称
        elif zigflag == 4:
            temp_right += CYCLE_AN
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += -CYCLE_AN    #　左右対称
        elif zigflag == 5:
            temp_right += 0
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += 0    #　左右対称
        elif zigflag == 6:
            temp_right += CYCLE_AN
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += -CYCLE_AN    #　左右対称
        elif zigflag == 7:
            temp_right += 0
            #temp_left += -CYCLE_AN  #　左右非対称
            temp_left += 0   #　左右対称

    curr_time = input_time()
    serial_connect(temp_right, temp_left)
    temp_right = RIGHT_INIT + 90
    temp_left = LEFT_INIT + 90

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the Roomba...")

def listener():
    rospy.init_node('nodemain', anonymous=True)

    #cmd_JCへのメッセージを受け取るとdecide_angleを実行
    rospy.Subscriber('joy', Joy, decide_angle)
    #cmd_ACへのメッセージを受け取るとcallback1を実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    #musicノードから
    rospy.Subscriber('cmd_MC', Int16, music_log)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    time.sleep(1.5) # Arduinoの起動時間待機
    program_start_time = input_time()
    listener()
