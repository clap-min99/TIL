# 최소이동거리 구하기
from collections import deque

def get_road_move_time(road, n, m):
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 도착지점 n-1, m-1
    queue = deque([0, 0])

    # visited 겸 복사. 각 좌표마다 걸리는 최소 이동 시간을 저장하는 2차원 리스트
    # 꼭 -1이 아니어도 상관 없다.
    distance = [[-1]*m for _ in range(n)]
    distance[0][0] = 0  # 처음 방문 찍기. 아직 안움직였으니까 0부터 시작(-1을 0으로 바꿈)

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if road[nx][ny] == 0:
                continue
            if distance[nx][ny] != -1:
                continue
            queue.append((nx, ny))
            distance[nx][ny] = distance[x][y] +1

            if nx == n-1 and ny == m-1:
                return distance[nx][ny]
    return -1
