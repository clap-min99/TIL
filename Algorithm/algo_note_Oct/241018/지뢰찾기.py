# 1996 지뢰찾기

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
print(arr)
visited= [[0]*N for _ in range(N)]

dij = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]

def bomb(i, j):
    pass
    