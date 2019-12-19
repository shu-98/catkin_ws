ラズパイ側
・ar_roomba.launch (teleop, roomba500)
・main_node

PC側
・roscore
・joy_node
・cycle_node
・roslaunch arduino_roomba ar_music.launch (wave_music, timing, vibration)
・roslaunch arduino_roomba ar_log.launch (imu_read, write_log)

ar_roomba.launchの前には，
・ラズパイにシリアルケーブルを挿す
・sudo chmod 777 /dev/ttyUSB0
・ルンバの電源をつける

joy_nodeの前には，
・ds4を有線で挿す（何故か無線だとタッチパネルの入力しかとってくれない&「ds4dr」を使うと振動機能が使えないらしい）

joyの入力が来てるか確認
・rostopic echo /joy

振動来るか確認
・sudo fftest /dev/input/eventX    ## Xには任意の数字
・"cat /proc/bus/input/devices"でeventの番号を調べられる.

音が出ない
・alsamixer  (十字キーでスピーカなど選んで"m"でミュート解除&十字キー上で"headphone"の音量をMAXに)
*内蔵スピーカから音を出すことは結局できなかった.（外部スピーカならいけるので実験には支障ない？）
・"sudo alsactl store"で音量設定を保存.再起動後もそのまま使える（らしい）

"rosrun arduino_roomba main_node.py"で"~~, try sudo?"って言われる（ラズパイのGPIOはスーパーユーザしか利用できない）
・rosrunがsudoで実行できない
・・"sudo -s"でrootユーザとしてログインし,ユーザ名が#になっている場合,rosrunできるはず.

やたらpingが高い時がある
・"sudo iwconfig wlp2s0 power off"でpower management機能をオフにすると早くなる（可能性がある）.

カメラのオートフォーカスなどの設定ができない
・v4l2-ctl -d /dev/videoX --list-ctrls (Xは任意の番号)
・v4l2-ctl -d /dev/videoX --set-ctrl=Y=Z (Yがカメラの設定名称,Zはvalue)
参考文献：https://www.kurokesu.com/main/2016/01/16/manual-usb-camera-settings-in-linux/

BLEの加速度センサの使い方
・マイコンに電源を挿す
・ubuntuのBluetoothの新規作成から"ESP32"を探す（なぜか接続済みの方からは接続できない）
・"sudo rfcomm bind 1 30:AE:A4:1F:1F:6A"
・"sudo chmod 777 /dev/rfcomm1"
・"rosrun arduino_roomba imu_read.py"
