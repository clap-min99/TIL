# 15650 N과 M
from itertools import combinations
N, M = map(int, input().split())
N_lst = [i for i in range(1, N+1)]
subset = combinations(N_lst, M)
subset = list(subset)
for i in range(len(subset)):
    print(*subset[i])