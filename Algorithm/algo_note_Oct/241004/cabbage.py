# 1012 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(i, j):
    dij = [[0, 1],[-1, 0],[0, -1],[1, 0]]
    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if 0<= ni < N and 0<= nj < M:
            if cabbage[ni][nj] == 1:
                cabbage[ni][nj] = 0
                dfs(ni, nj)
        

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    visited = [[0]*M for _ in range(N)]
    cabbage = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
    
  

