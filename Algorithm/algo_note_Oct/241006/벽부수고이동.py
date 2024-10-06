# 2206 벽 부수고 이동하기

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]

dij = [[0,1],[-1,0],[0,-1],[1,0]]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs(i,j,k):
    q = deque()
    q.append((i,j,k))

    while q:
        x, y, z = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        
        for di, dj in dij:
            ni = x + di
            nj = y + dj

            if ni<0 or ni >= N or nj<0 or nj>=M:
                continue
            
            # 부술 기회가 한번 있고, 다음 이동할 곳이 벽일 때
            if map[ni][nj] == 1 and z == 0:
                visited[ni][nj][1] = visited[x][y][0] + 1
                q.append((ni,nj,1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳일 때
            elif map[ni][nj] == 0 and visited[ni][nj][z] == 0:
                visited[ni][nj][z] = visited[x][y][z] + 1
                q.append((ni,nj,z))
    return -1

print(bfs(0,0,0))