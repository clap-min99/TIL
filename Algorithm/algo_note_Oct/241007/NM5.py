# 15654 N과 M(5)
from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(map(int, input().split()))

arrs = list(permutations(nums, M))
for i in range(len(arrs)):
    print(*arrs[i])
