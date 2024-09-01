
# 방법 1
# N = int(input())
#
# arr = []
# zero = 0
#
# for i in range(N):
#     x = int(input())
#     if x != 0:
#         arr.append(x)
#     if x == 0:
#         if not arr:
#             print(0)
#             continue
#         arr.sort()
#         arr.reverse()
#         print(arr.pop())
# 시간 초과


# 방법 2
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    if x != 0:
        heappush(heap, x)
