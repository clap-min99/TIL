# 10026 적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
pic = [list(input().strip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dij = [[0,1],[0,-1],[1,0],[-1,0]]
cnt = 0
def dfs(i, j):
    
    visited[i][j] = 1

    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if pic[ni][nj] == pic[i][j] and not visited[ni][nj]:
            dfs(ni, nj)
     

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            cnt += 1


# R을 G로 바꾸어줌 
for i in range(N):
    for j in range(N):
        if pic[i][j] == 'R':
            pic[i][j] = 'G'

# 적록색맹 dfs
c_blind = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            c_blind += 1

print(cnt, c_blind)