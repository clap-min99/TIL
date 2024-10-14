# 15663 N과M(9) 
import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

nums_arr = sorted(set(permutations(nums, M)))
for i in range(len(nums_arr)):
    print(*nums_arr[i])