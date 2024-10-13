# 15666 N과M12

import sys
input = sys.stdin.readline
from collections import deque


def arr(length):
    if len(temp) == M:
        print(*temp)
        return
    
    for i in range(len(nums)):
        if length == 0 or temp[-1] <= nums[i]:
            temp.append(nums[i])
            arr(length+1)
            temp.pop()

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))
temp = []

arr(0)