#21736 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dij = [[0,1],[1,0],[-1,0],[0,-1]]

# 시작점 찾기
def start(arr):
    for i in range(N):
        for j in range(M):
            for di, dj in dij:
                ni = i + di
                nj = j + dj
                if 0<= ni < N and 0 <= nj < M and arr[ni][nj] == 'I':
                    return ni, nj


def find(a, b):
    global cnt
    visited[a][b] = 1
    if map[a][b] == 'P':
        cnt += 1

    for di, dj in dij:
        na = a + di
        nb = b + dj
        if 0<= na < N and 0<= nb <M and not visited[na][nb]:
            if map[na][nb] != 'X':
                find(na, nb)


N, M = map(int, input().split())
map = [list(input())[:-1] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
x, y = start(map)
find(x, y)
if cnt == 0:
    print('TT')
else:
    print(cnt)