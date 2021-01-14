"""
3×3のサイズのビンゴカードが、最終的にビンゴしているかどうかを判定する問題です。
入力
3
oox
xoo
oxo

oox
xoo
ooo

Yes
"""
import sys

N = int(input()) # 入力回数をNとして受け取る
list = [input() for i in range(N)]
#print(list) ->['oxox', 'xxox', 'ooxo', 'oooo']
cnt = 0

try:
    for i in range(N): #もしtryの上にこれ書くと一つずつYesNo判定されてしまう。
        if list[i].count('o') == N:
            print('Yes')
            break
finally:
    if list[i].count('o') != N: #必須。なんでiがこの位置にあるのに正確に動くのか分からない。
        print('No')

    # list[i].count('x') >= 1:
    #   print('debag')
    #でもいい。



"""
4
oxox
xxox
ooxo
ooox

4
oxox
xoox
oxoo
ooxo


oxox
xxox
ooxo
oooo

oooo
oxox
xxox
ooxo
#a = [[str(c) for c in l.strip()] for l in sys.stdin]
"""