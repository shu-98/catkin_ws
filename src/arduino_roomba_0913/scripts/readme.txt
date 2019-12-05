ラズパイ側
・ar_roomba.launch
・main_node

PC側
・roscore
・vibration_node
・joy_node
・cycle_node
・roslaunch arduino_roomba ar_music.launch
・write_log

ar_roomba.launchの前には，
・ラズパイにシリアルケーブルを挿す
・sudo chmod 777 /dev/ttyUSB0
・ルンバの電源をつける

joy_nodeの前には，
・ds4を有線で挿す（何故か無線だとタッチパネルの入力しかとってくれない&「ds4dr」を使うと振動機能が使えないらしい）

joyの入力が来てるか確認
・rostopic echo /joy

振動来るか確認
・fftest /dev/input/eventX    ## Xには任意の数字

音が出ない
・alsamixer  (十字キーでスピーカなど選んで"m"でミュート解除&十字キー上で"headphone"の音量をMAXに)
*内蔵スピーカから音を出すことは結局できなかった.（外部スピーカならいけるので実験には支障ない？）

"rosrun arduino_roomba main_node.py"で"~~, try sudo?"って言われる（ラズパイのGPIOはスーパーユーザしか利用できない）
・rosrunがsudoで実行できない
・・"sudo -s"でrootユーザとしてログインし,ユーザ名が#になっている場合,rosrunできるはず.
