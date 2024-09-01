# 최소이동거리 구하기
from collections import deque


def get_road_move_time(road, n, m):
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[False]*m for _ in range(n)]
    # 도착지점 n-1, m-1
    queue = deque([0, 0, 0])
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in dxy:
            # 갈 수 있는 곳이라면 (nx, ny, n_dist)를 저장한다.
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if road[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            queue.append((nx, ny))
            distance[nx][ny] = distance[x][y] + 1

            if nx == n - 1 and ny == m - 1:
                return distance[nx][ny]
    return -1