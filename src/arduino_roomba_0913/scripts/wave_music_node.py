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
wavfile = "/home/roomba/catkin_ws/src/arduino_roomba/scripts/music/Call_Me_Maybe.wav"

pub = rospy.Publisher('cmd_MC', Int16, queue_size=10)

# WAVファイルを開く
wf = wave.open(wavfile, "rb")

# PyAudioのインスタンスを生成 (1)
p = pyaudio.PyAudio()

# 再生用のコールバック関数を定義 (2)
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

def music(data):
    global wf

    #time.sleep(0.3)
    #time.sleep(0.38) #OC一日目
    #time.sleep(0.08) #OC二日目
    #time.sleep(0.25) #同じ部屋
    #time.sleep(0.20) #別部屋8/30
    #time.sleep(0.25) #別部屋9/05
    time.sleep(0.5) #別部屋9/07 #Skype2台

    # Streamを生成(3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # Streamをつかって再生開始 (4)
    stream.start_stream()
    rospy.loginfo("Starting music...")

    # 再生中はひとまず待っておきます (5)
    #while stream.is_active():
    #    time.sleep(0.1)
    time.sleep(190)

    rospy.loginfo("Stopping music...")
    # 再生が終わると、ストリームを停止 (6)
    stream.stop_stream()
    stream.close()
    rospy.loginfo("Stopping music...")

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the MusicNode...")

    # 再生が終わると、ストリームを解放 (6)
    wf.close()

    # close PyAudio (7)
    p.terminate()

def listener():
    rospy.loginfo("listener()")
    #cmd_JCへのメッセージを受け取るとdecide_angleを実行
    rospy.Subscriber('cmd_M', Int16, music)
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('music', anonymous=True)
    listener()
