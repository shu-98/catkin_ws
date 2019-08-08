#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
import pygame.mixer
import threading
import time
import datetime

pub = rospy.Publisher('cmd_MC', Int16, queue_size=10)

def music(data):
    #time.sleep(0.3)
    #time.sleep(0.38) #OC一日目
    #time.sleep(0.08) #OC二日目
    #time.sleep(0.25) #同じ部屋
    #time.sleep(0.20) #別部屋8/30
    #time.sleep(0.25) #別部屋9/05
    time.sleep(0.475) #別部屋9/07 #Skype2台
    pygame.mixer.init()
    pygame.mixer.music.load('/home/roomba/catkin_ws/src/roomba_st/scripts/music/Call_Me_Maybe.mp3') #　パスの最後を再生したい曲にする
    pygame.mixer.music.play(-1) # ()内は再生回数 -1:ループ再生

    rospy.loginfo("Starting music...")
    pub.publish(1)
    #time.sleep(20)
    time.sleep(190)
    pygame.mixer.music.stop() # 再生の終了
    rospy.loginfo("Stopping music...")

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the MusicNode...")

def listener():
    rospy.loginfo("listener()")
    #cmd_JCへのメッセージを受け取るとdecide_angleを実行
    rospy.Subscriber('cmd_M', Int16, music)
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('music', anonymous=True)
    listener()
