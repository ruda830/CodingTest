N = int(input())
a = sorted(map(int, input().split()))[::-1] #降順に並べる。
print(sum(a[::2]) - sum(a[1::2]))