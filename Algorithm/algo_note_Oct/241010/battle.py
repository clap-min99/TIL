# 1303 전쟁-전투
import sys
input = sys.stdin.readline

dij = [[0,1],[-1,0],[0,-1],[1,0]]

def force(i, j):
    global b, w
    visited[i][j] = 1
    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= M or nj < 0 or nj >= N:
            continue
        if war[i][j] == 'W':
            if war[ni][nj] == 'W' and not visited[ni][nj]:
                w += 1
                force(ni, nj)
        elif war[i][j] == 'B':
            if war[ni][nj] == 'B' and not visited[ni][nj]:
                b += 1
                force(ni, nj)


N, M = map(int, input().split())
war = [list(map(str, input().strip())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
my_team = 0
enemy = 0
w, b = 0, 0
for i in range(M):
    for j in range(N):
        if war[i][j] == 'W' and not visited[i][j]:
            w = 1
            force(i, j)
            my_team += w**2
        elif war[i][j] == 'B'and not visited[i][j]:
            b = 1
            force(i, j)
            enemy += b**2
        w, b = 0, 0
print(my_team, enemy)