#!/usr/bin/env python
#coding:utf-8

import rospy
import pygame.mixer
import time

rospy.init_node('music', anonymous=True)
pygame.mixer.init()
pygame.mixer.music.load('/home/roomba/catkin_ws/src/roomba_st/scripts/music/Call_Me_Maybe.mp3') #　パスの最後を再生したい曲にする
pygame.mixer.music.play(-1) # ()内は再生回数 -1:ループ再生

#pygame.mixer.music.pause() # 音楽の一時停止
#pygame.mixer.music.unpause # 一時停止した音楽の再開
#pygame.mixer.music.set_volume(0.8) # ボリュームの設定
#pygame.mixer.music.queue('test2.mp3') # 次の再生ファイルのセット

rospy.loginfo("Starting music...")
time.sleep(1200) #　20分
pygame.mixer.music.stop() # 再生の終了
rospy.loginfo("Stopping music...")
