# #4875 파이썬 문제해결 기본 5일차(미로)

def path(i, j, N):
    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if path(ni, nj, N):
                    return 1
        return 0


def start_p(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = start_p(N)
    visited = [[0] * N for _ in range(N)]
    ans = path(sti, stj, N)

    print(f'#{tc} {ans}')


