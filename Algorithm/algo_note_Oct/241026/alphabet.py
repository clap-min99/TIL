# 1987 알파벳
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

dij = [[0,1],[1,0],[0,-1],[-1,0]]
cnt = 1
def alp(i, j):
    global cnt
    visited[i][j] = board[i][j]
    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            continue
        if board[ni][nj] in visited:
            break
       
        elif board[ni][nj] not in visited:
            alp(ni, nj)
alp(0,0)

print(cnt)