import sys
input = sys.stdin.readline
from collections import deque

dij = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1],[1,1],[-1,-1]]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for di, dj in dij:
            ni = x + di
            nj = y + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue

            if island[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1
                


while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    island = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)