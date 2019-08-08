#!/usr/bin/env python
#coding:utf-8

import pygame.mixer
import time

if __name__ == "__main__":
    rospy.init_node('nodeA', anonymous=True)
    pygame.mixer.init()
    pygame.mixer.music.load('/home/roomba/catkin_ws/src/learning_joy/scripts/02 - Alchemy.mp3')
    pygame.mixer.music.play(1) # ()内は再生回数 -1:ループ再生
    time.sleep(420)
