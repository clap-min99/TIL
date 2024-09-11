# 2178 미로탐색
from collections import deque

def search():
    dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque()
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if maze[ni][nj] == 1:
                maze[ni][nj] = maze[i][j] + 1
                q.append((ni, nj))


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

maze[0][0] = 1
search()
ans = maze[N-1][M-1]
print(ans)
