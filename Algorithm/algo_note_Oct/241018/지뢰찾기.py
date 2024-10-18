# 1996 지뢰찾기
from pprint import pprint
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

        


visited= [[0]*N for _ in range(N)]

dij = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]

def bomb(i, j):
    
    a = 0

    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni>= N or nj <0 or nj >= N:
            continue
        if arr[ni][nj].isnumeric():
            a += int(arr[ni][nj])

    if a<10:
        visited[i][j] = a
    else: 
        visited[i][j] = 'M'

for i in range(N):
    for j in range(N):
        if arr[i][j].isnumeric():
            visited[i][j] = '*'
        else:
            bomb(i,j)


for a in visited:
    cnt = 0
    for b in a:
        print(b, end="")
        cnt += 1
        if cnt == N:
            print()

        