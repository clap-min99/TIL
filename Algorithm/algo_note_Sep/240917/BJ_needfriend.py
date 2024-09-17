import sys
input = sys.stdin.readline
dij = [[0,1],[1,0],[-1,0],[0,-1]]

def start(arr):
    for i in range(N):
        for j in range(M):
            for di, dj in dij:
                ni = i + di
                nj = j + dj
                if 0<= ni < N and 0 <= nj < M and arr[ni][nj] == 'I':
                    return ni, nj
                    


N, M = map(int, input().split())
map = [list(input())[:-1] for _ in range(N)]
x, y = start(map)
print(x, y)