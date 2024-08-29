import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x != 0:
        heappush(heap, -x)
    else:
        if not heap:
            print(0)
            continue
        print(-heappop(heap))

