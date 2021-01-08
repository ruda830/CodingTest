
# -*- coding: utf-8 -*-
"""
入力
a b

出力
偶数なら
Even
奇数なら
Odd
"""

a, b = map(int, input().split())

if a*b%2==0:
  print('Even')
else:
  print('Odd')