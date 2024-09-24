# 7576 토마토
import sys
input = sys.stdin.readline
from collections import deque


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dij = [(0,1),(1,0),(0,-1),(-1,0)]
visited = [[0]*M for _ in range(N)]
start = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start.append([i, j])

ans = 0
def toma():
    while start:        
        x, y = start.popleft()
        for di, dj in dij:
            ni = x + di
            nj = y + dj 
            if 0<= ni < N and 0 <= nj <M:
                if tomato[ni][nj] == 0:
                    tomato[ni][nj] = tomato[x][y] + 1
                    start.append([ni, nj])
                    
toma()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)