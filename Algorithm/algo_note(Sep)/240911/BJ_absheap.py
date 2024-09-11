# 11286 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            print(0)
        else:
            a = heapq.heappop(q)
            print(a[1])
