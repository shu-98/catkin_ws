#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
import pygame.mixer
import threading
import time
import datetime

# -*- coding: utf-8 -*-
import wave
import pyaudio
import time
input_filename = "/home/roomba/catkin_ws/src/arduino_roomba/scripts/music/Call_Me_Maybe.wav"
buffer_size = 4096

cnt = 0

def music(data):
    global cnt

    #time.sleep(0.3)
    #time.sleep(0.38) #OC一日目
    #time.sleep(0.08) #OC二日目
    #time.sleep(0.25) #同じ部屋
    #time.sleep(0.20) #別部屋8/30
    #time.sleep(0.25) #別部屋9/05
    time.sleep(0.13) #別部屋9/07 #Skype2台
    time.sleep(cnt*0.03)

    rospy.loginfo("Starting music...")

    wav_file = wave.open ( input_filename , 'rb' )
    p = pyaudio.PyAudio ()
    stream = p.open (
                     format = p.get_format_from_width ( wav_file . getsampwidth ()) ,
                     channels = wav_file.getnchannels () ,
                     rate = wav_file.getframerate () ,
                     output = True
                     )
    remain = wav_file.getnframes ()
    while remain > 0:
        buf = wav_file.readframes ( min ( buffer_size , remain ))
        stream.write ( buf )
        remain -= buffer_size

    stream.close ()
    p.terminate ()
    wav_file.close ()
    rospy.loginfo("Stopping music...")
    cnt += 1

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the MusicNode...")

    #p.terminate ()
    #wav_file.close ()

def listener():
    rospy.loginfo("listener()")
    #cmd_JCへのメッセージを受け取るとdecide_angleを実行
    rospy.Subscriber('cmd_M', Int16, music)
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('music', anonymous=True)
    listener()
