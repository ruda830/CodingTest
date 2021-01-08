
# -*- coding: utf-8 -*-
"""
入力
a
b c
s
出力
a+b+c s
"""

a = int(input())
b, c = map(int, input().split())
s = input()
print("{} {}".format(a+b+c, s))