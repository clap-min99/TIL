import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = [[-1]*m for _ in range(n)]
def start(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                a, b = i, j
            return a, b

# 원래 0 인 지점은 0으로 표시
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans[i][j] = 0


a, b = start(arr)        
q = deque([])
q.append((a, b))
visited[a][b] = 1
ans[a][b] = 0
dxy = [[0,1], [-1,0],[0, -1], [1, 0]]
def dist(arr):
    while q:
        x, y = q.popleft()    
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    ans[nx][ny] = ans[x][y] + 1
                    q.append((nx, ny))

dist(arr)
for row in ans:
    print(*row)
