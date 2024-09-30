# 2667 단지번호 붙이기
import sys
input = sys.stdin.readline
from collections import deque


dij = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(si, sj):
    q = deque([])
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
       i, j = q.popleft()
       for di, dj in dij:
            ni, nj = i+di, j+dj
            if 0<= ni < N and 0<= nj<N and visited[ni][nj]==0 and map[ni][nj]==1:
                q.append((ni,nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]


visited = [[0]*N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i,j))
ans.sort()

print(len(ans))
print(*ans, sep='\n')

