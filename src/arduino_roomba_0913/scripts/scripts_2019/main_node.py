#!/usr/bin/env python
# coding:utf-8

## GPIOピン(18,19)に繋げればそのあま使える？

import rospy
from std_msgs.msg import Int16
import datetime
import sys
import wiringpi
import subprocess

# サーボモータに接続したGPIO端子番号を指定
servo_pin1  =  12
servo_pin2  =  13
# サーボモータを動かす角度を指定する
set_degree = 0
wiringpi.wiringPiSetupGpio()
# ハードウェアPWMで出力する
wiringpi.pinMode( servo_pin1, 2 )
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
SERVO_INIT = 60
CYCLE_AN = 15
zigflag = 0

#　平行になる値
temp_right = SERVO_INIT
temp_left = SERVO_INIT

cy_curr_time = 500.0
cy_prev_time = 0.0

cycle_first_flag = 1

print("init-option")
print("")

def input_time():
    t = datetime.datetime.today()
    d = t.hour*3600 + t.minute*60 + t.second +  t.microsecond*0.000001
    return d

def serial_connect(data_right, data_left):
    # print("%s, %s" % (data_left, data_right))
    # 角度から送り出すPWMのパルス幅を算出する
    move_deg1 = int( 81 + 41 / 90.0 * data_right )
    move_deg2 = int( 81 + 41 / 90.0 * data_left )
    print("%s, %s" % (move_deg1, move_deg2))
    # サーボモータにPWMを送り、サーボモータを動かす
    wiringpi.pwmWrite( servo_pin1, move_deg1 )
    wiringpi.pwmWrite( servo_pin2, move_deg2 )
    ## GPIO

def callback(data):
    global zigflag

    global temp_right
    global temp_left

    global cycle_first_flag
    global cy_prev_time
    global cy_curr_time

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
            temp_right += CYCLE_AN
            temp_left += -CYCLE_AN
            zigflag = 1
        elif zigflag == 1:
            temp_right += 0
            temp_left += 0
            zigflag = 0

    serial_connect(temp_right, temp_left)
    temp_right = SERVO_INIT
    temp_left = SERVO_INIT

def shutdown():
    # Always stop the Roomba when shutting down the node.
    wiringpi.pwmWrite( servo_pin1, 0 )
    wiringpi.pwmWrite( servo_pin2, 0 )
    subprocess.call("gpio -g mode %s IN" % (servo_pin1), shell=True)
    subprocess.call("gpio -g mode %s IN" % (servo_pin2), shell=True)
    rospy.loginfo("Stopping robot's ears...")

def listener():
    rospy.init_node('nodemain', anonymous=True)

    #cmd_ACへのメッセージを受け取るとcallback1を実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    listener()
