# 4963 섬의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dij = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1],[1,1],[-1,-1]]

def dfs(x, y):
    visited[x][y] = 1
    for di, dj in dij:
        ni, nj = x+di, y+dj

        if ni<0 or ni>=h or nj <0 or nj>= w:
            continue

        if island[ni][nj] == 1 and not visited[ni][nj]:
            dfs(ni, nj)
            

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = [list(map(int, (input().split()))) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0 

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    
    print(cnt)

    # recursion error;;