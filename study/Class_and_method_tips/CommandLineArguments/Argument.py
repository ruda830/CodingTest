"""
コマンドライン引数にファイルを入れる場合の処理
$ python Argument.py a b c
"""
import sys
args = sys.argv

print(args)
print("実行ファイル：" + args[0])
print("第一引数：" + args[1])
print("第二引数：" + args[2])
print("第三引数：" + args[3])
