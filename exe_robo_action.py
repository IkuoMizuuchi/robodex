# -*- coding: utf-8 -*-
import TableRobotAction

#以下、不要なものもあるはず。
import requests
import json
import os
import subprocess
#commandsは、python3ではsubprocessに内包された
#import commands

#
def execute_robot_action(robot_action):
    #robot_actionを通し番号として、テーブルに書かれた動作をする。
    #話す、首振り動作、LED点灯

    if robot_action = (0,0,0):
        return

    elif 1 == robot_action(0):
        message = '何か伺いましょうか？'
        check = commands.getoutput('curl "https://api.voicetext.jp/v1/tts" -s -u 563fw3j9tnberqyq: -d speed=100 -d speaker=hikari -d "text=%s" | aplay 2> /dev/null '% speak_message)

    else:
        pass

#csvファイルのテーブルを開いて、通し番号に対応するデータを持ってくる
class GetRobotActionDataOfComment:

        def __init__(self):
                robot_action_data_of_comment = ""

        def getRobotComment(self,comment_tbl_no):
		#ここで、csvなどのテーブルファイルを開き、comment_tbl_noに対応するコメントを返り値の変数に入れる

                return self.robot_action_data_of_comment
