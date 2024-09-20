import sys
input = sys.stdin.readline
from collections import deque


M, N = int(input())
tomato = [list(map(int, input().split())) for _ in range(N)]
dij = [(0,1),(1,0),(0,-1),(-1,0)]
visited = [[0]*M for _ in range(N)]
start = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start.append([i, j])

ans = 0

    