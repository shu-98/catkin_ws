#!/usr/bin/env python
# coding:utf-8

import fcntl, struct, array, time
import rospy
from std_msgs.msg import Int16

## /dev/input/eventX の"X"を任意のやつを変える ##
EVENT_NUM = "/dev/input/event14"

EVIOCRMFF = 0x40044581
EVIOCSFF = 0x40304580
LOG_CLASS_ON = False
TIME_DELTA = 100

import signal
from twisted.internet import task, reactor

INTERVAL = rospy.get_param("interval", 0.5)
SLEEP = 0.36    ## BGMに合わせるため

cycle_first_flag = 1

class Vibrate:  ## 振動用のクラス,どっかから引っ張ってきたのでよくわからん

    def __init__(self, file):
        self.ff_joy = open(file, "r+")

    def close(self):
        self.ff_joy.close()

    def new_effect(self, strong, weak, length):
        effect = struct.pack('HhHHHHHxHH', 0x50, -1, 0, 0, 0, length, 0, int(strong * 0xFFFF), int(weak * 0xFFFF))
        a = array.array('h', effect)
        fcntl.ioctl(self.ff_joy, EVIOCSFF, a, True)
        return a[1]
        id = a[1]
        return (ev_play, ev_stop)

    def play_efect(self, id):
        if type(id) == tuple or type(id) == list:
            ev_play = ''
            for i in id:
                ev_play = ev_play + struct.pack('LLHHi', 0, 0, 0x15, i, 1)
        else:
            ev_play = struct.pack('LLHHi', 0, 0, 0x15, id, 1)
        self.ff_joy.write(ev_play)
        self.ff_joy.flush()

    def stop_effect(self, id):
        if type(id) == tuple or type(id) == list:
            ev_stop = ''
            for i in id:
                ev_stop = ev_stop + struct.pack('LLHHi', 0, 0, 0x15, i, 0)
        else:
            ev_stop = struct.pack('LLHHi', 0, 0, 0x15, id, 0)
        self.ff_joy.write(ev_stop)
        self.ff_joy.flush()

    def forget_effect(self, id):
        if type(id) == tuple or type(id) == list:
            for i in id:
                fcntl.ioctl(self.ff_joy, EVIOCRMFF, i)
        else:
            fcntl.ioctl(self.ff_joy, EVIOCRMFF, id)

t1 = TIME_DELTA / 1000.0 * 1/7
t2 = TIME_DELTA / 1000.0 * 1/7
t3 = TIME_DELTA / 1000.0 * 3/7

f = Vibrate(EVENT_NUM)
p = f.new_effect(0.0, 1.0, TIME_DELTA )
p1 = f.new_effect(0.0, 0.1, t1 )
p2 = f.new_effect(0.0, 0.4, t2 )
p3 = f.new_effect(0.0, 1.0, t3 )

def vibration_power(event, event_time):
    f.play_efect(event)
    time.sleep(event_time)
    f.stop_effect(event)

def loop():
    print("Vib!")
    vibration_power(p1, t1)
    vibration_power(p2, t2)
    vibration_power(p3, t3)
    vibration_power(p2, t2)
    vibration_power(p1, t1)

def loop_start():
    # 実行間隔
    interval = INTERVAL

    time.sleep(SLEEP)

    # ループに関数を登録して、指定された間隔で実行する
    instance = task.LoopingCall(loop)
    instance.start(interval)

    # twistedのイベントループを開始する
    reactor.run()

    signal.signal(signal.SIGINT, handler)
    signal.pause()

def callback(data):
    global cycle_first_flag

    if cycle_first_flag == 1:
        cycle_first_flag = 0
        loop_start()

def shutdown():
    f.forget_effect((p))
    # Always stop the Roomba when shutting down the node.
    rospy.loginfo("Stopping the Vibration...")

if __name__ == '__main__':
    rospy.init_node('node_vib', anonymous=True)

    #cmd_ACへのメッセージを受け取るとcallback1を実行
    rospy.Subscriber('cmd_AC', Int16, callback)
    #ノードの停止処理を実行
    rospy.on_shutdown(shutdown)
    rospy.spin()
