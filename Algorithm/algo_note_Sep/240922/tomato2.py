# 7569 토마토
import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
tomato= [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dijk = [[1,0,0],[0,1,0],[-1,0,0],[0,-1,0],[0,0,1],[0,0,-1]]
q = deque([])


for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append((i,j,k))

def toma():
    while q:
        z, x, y = q.popleft()
        for dx, dy, dz in dijk:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0<= nx < N and 0<= ny <M and 0<= nz <H:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    q.append((nz, nx, ny))

toma()
ans = 0
check = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                check = True
            ans = max(ans, tomato[i][j][k])
if check:
    print(-1)
else:
    print(ans-1)