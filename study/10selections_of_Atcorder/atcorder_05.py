
# -*- coding: utf-8 -*-
"""
500円　A枚
100円　B枚
50円　C枚

入力
A
B
C
X
出力
コインを選ぶ方法の数
"""
#＃動的計画法

#4要素をリストに入れる。
A, B, C, X =[int(input()) for i in range(4)]
cnt = 0
#総当たり
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if X == a*500 + b*100 + c*50:
                #インクリメント処理
                cnt += 1

print(cnt)