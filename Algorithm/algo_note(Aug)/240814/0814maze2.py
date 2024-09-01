from collections import deque


def start_p(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(arr, i, j):
    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque([i, j])
    visited[i][j] = 1       # 현재 노드 방문 처리

    while q:
        i, j = q.popleft()
        for di, dj in dij:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= N or nj <0 or nj >= N:  # 범위를 벗어나는 경우
                continue
            if arr[ni][nj] == 1:         # 길이 아닌 경우
                continue
            if visited[ni][nj] != -1:    # 이미 방문한 곳인 경우
                continue

            q.append((ni, nj))
            visited[ni][nj] = 1

            if visited[ni][nj] == 3:
                return 1
            else:


    return 0


T = 10
N = 100
for test in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    sti, stj = start_p(N)
    ans = bfs(maze, sti, stj)