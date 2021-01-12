
# -*- coding: utf-8 -*-
"""
500円　A枚
100円　B枚
50円　C枚

入力
N A B
出力
10進法での各桁の和がA以上B以下であるものの総和
"""

N, A, B = map(int, input().split())
ans = 0
for i in range(N+1):
    #ここが分からん
    if A <= sum(list(map(int, str(i)))) <= B:
        ans += i
print(ans)
