"""
2
1 4 2 5
"""

"""
4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4
"""
"""
例
4
6 12 13 5 3 17 10 11 16 9 8 15 2 1 14 4
"""

N = int(input())
l = list(map(int, input().split()))

a = l[:len(l)//2]
b = l[len(l)//2:]
A = max(a)
B = max(b)

#print(B if A>B else A)
print(l.index(B)+1 if A > B else a.index(A)+1)