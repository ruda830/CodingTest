"""
#標準入力と内包表記について慣れる。
sys.stdinの練習


data_list = [ [int(s) for s in line.split()] for line in sys.stdin ]
print(data_list)

inp=input('なんか入力しろ>')
"""
import sys
#data_list = [ [int(s) for s in line.split()] for line in sys.stdin ]

for line in sys.stdin:
    print(line)