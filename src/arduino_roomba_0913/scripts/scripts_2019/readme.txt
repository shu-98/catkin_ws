ラズパイ側
・ar_roomba.launch
・main_node

PC側
・joy_node
・cycle_node
・vibration_node
・ar_music.launch(?)
・write_log

ar_roomba.launchの前には，
・ラズパイにシリアルケーブルを挿す
・sudo chmod 777 /dev/USB0
・ルンバの電源をつける

joy_nodeの前には，
・ds4を有線で挿す（何故か無線だとタッチパネルの入力しかとってくれない&「ds4dr」を使うと振動機能が使えないらしい）

joyの入力が来てるか確認
・rostopic echo /joy

振動来るか確認
・fftest /dev/input/eventX    ## Xには任意の数字
