"""
コマンドライン引数にファイルを入れる場合の処理
$ python arg_file.py arg_file.json

参考URL:https://qiita.com/u1and0/items/ce5fa6229e2cfa55d3c6
"""
import sys
import json

args = sys.argv
json_f = json.load(args[1])
print(json_f)

import sys
import fileinput
from pathlib import Path




if Path(sys.argv[1]).exists():  # 第一引数がファイルだったら
    for line in fileinput.input():  # ファイルの内容を一行ずつprint
        print('file input')
        print(line)

import json

json_open = open('qitta_json.json', 'r')
json_load = json.load(json_open)

print(json_load)

"""
import sys
args = sys.argv

print(args)
print("実行ファイル：" + args[0])
print("第一引数：" + args[1])
"""

"""
F = sys.stdin
for line in F:
    print(line.strip("\n"))
"""