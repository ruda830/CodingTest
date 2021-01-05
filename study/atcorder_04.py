# -*- coding: utf-8 -*-
"""
入力
3
8 12 40
出力
2
"""

N = input()
#aはイテラブル
a = list(map(int, input().split()))
cnt = 0
#全ての要素が真ならば
while all(i%2==0 for i in a):
    a = [i/2 for i in a]
    cnt += 1

print(cnt)
