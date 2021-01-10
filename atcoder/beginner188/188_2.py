"""
2
-3 6
4 2

"""
"""
for i in range(n):
    ans = 0
    #ans += a[i] * b[i] これだとiが2回計算されるっぽいなので、ダメ

    print(ans)
    print('Yes' if ans == 0 else'No')
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

for x, y in zip(a,b):
    ans += x * y

print('Yes' if ans == 0 else 'No')