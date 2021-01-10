x,y = map(int, input().split())
if x>y:
    result = x-y
    print('Yes' if result < 3 else 'No')
else:
    result = y-x
    print('Yes' if result < 3 else 'No')

