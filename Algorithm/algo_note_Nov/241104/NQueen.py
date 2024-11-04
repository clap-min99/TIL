# 9663 N-Queen
import sys
input = sys.stdin.readline
N = int(input())

def check(row, col):
    for i in range(row):
        if visited[i][col] == 1:
            return False

    # 왼쪽 대각선
    i, j = row -1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # 오른쪽 대각선
    i, j = row -1, col + 1
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1
        
    return True

def Nqueen(row):
    global cnt

    if row == N:
        cnt += 1
        return
    
    for col in range(N):
        if check(row, col):
            visited[row][col] = 1
            Nqueen(row+1)
            visited[row][col] = 0

visited = [[0]*N for _ in range(N)]
cnt = 0
Nqueen(0)
print(cnt)