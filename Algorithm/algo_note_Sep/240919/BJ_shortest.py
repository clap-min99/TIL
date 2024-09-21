# 14940 쉬운 최단거리
import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 시작 지점 찾기
def start(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                a, b = i, j
            return a, b

a, b = start(map)
visited = [[0]*m for _ in range(n)]
q = deque([])
q.append((a,b))
visited[a][b] = 0   
dxy = [[0,1], [-1,0],[0, -1], [1, 0]]
def distance(arr):
    while q:
        x, y = q.popleft()         
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
distance(map)

for row in visited:
    print(*row)

# Unboundlocal error;;; 
