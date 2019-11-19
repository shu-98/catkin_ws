#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
import threading
import time
import datetime

# -*- coding: utf-8 -*-
import wave
import pyaudio
import time
input_filename = "music/Call_Me_Maybe.wav"
buffer_size = 4096

cnt = 0

first_flag = 1
pub = rospy.Publisher('cmd_MC', Int16, queue_size=10)

def music(data):
    global cnt
    global first_flag

    time.sleep(0.13) #別部屋9/07 #Skype2台
    time.sleep(cnt*0.03)

    rospy.loginfo("Starting music...")
    if first_flag == 1:
        pub.publish(1)  ## main_nodeに音楽が開始したことを伝える（log用の）
        first_flag = 0
    else:
        pass

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
