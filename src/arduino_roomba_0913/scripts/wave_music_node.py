#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import Int16
import time
import datetime

import wave
import pyaudio

first_flag = 1

path = "/home/sou/catkin_ws/src/arduino_roomba_0913/scripts/music/"
music_name = rospy.get_param('music', "Call_Me_Maybe.wav")
input_filename = path + music_name
# input_filename = "/home/sou/catkin_ws/src/arduino_roomba_0913/scripts/music/Call_Me_Maybe.wav"
buffer_size = 4096  ## pyaudio に使うやつ（よくわからん）

pub = rospy.Publisher('cmd_MC', Int16, queue_size=10)

def music(data):
    global first_flag

    time.sleep(0.0) # 2019/11/19の調整

    if first_flag == 1:
        pub.publish(1)  ## main_nodeに音楽が開始したことを伝える（log用の）
        first_flag = 0
        if music_name == "Call_Me_Maybe.wav":
            time.sleep(0.10)
        if music_name == "180_metronome.wav":ll
            time.sleep(0.102)

        rospy.loginfo("Starting music...")
        pub.publish(1)  ## main_nodeに音楽が開始したことを伝える（log用の）

        ## よーわからんけどpyaudioの初期化
        try:
            while True:
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
                if music_name == "Call_Me_Maybe.wav":
                    time.sleep(0.15)
        except KeyboardInterrupt:
            p.terminate ()
            wav_file.close ()
            rospy.loginfo("Stopping music...")

def shutdown():
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the MusicNode...")

def listener():
    rospy.loginfo("listener()")
    ## cmd_ACへのメッセージを受け取るとmusicを実行
    rospy.Subscriber('cmd_AC', Int16, music)
    rospy.on_shutdown(shutdown)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('music', anonymous=True)
    listener()
