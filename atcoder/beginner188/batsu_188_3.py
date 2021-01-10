"""
2
1 4 2 5
"""

"""
4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4
"""
import numpy as np
N = int(input())
l = list(map(int, input().split()))
lN = int(2**N/2)
print(lN)

l_min = np.array(l).reshape(-1,2).tolist()
print(l_min)

for i in range(lN):
    val = max(l_min[i])
    print(type(val))

    """
    l_re = []
    ans = l_re.append(max(l_min[i]))
    print(ans)
    """

