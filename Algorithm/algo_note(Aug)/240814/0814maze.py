def find_path(i, j):
    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if find_path(ni, nj):
                    return 1
        return 0


def start_p(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1


T = 10
N = 16
for test in range(1, T+1):
    tc = int(input())
    visited = [[0] * N for _ in range(N)]
    maze = [list(map(int, input())) for _ in range(N)]
    sti, sij = start_p(N)
    ans = find_path(sti, sij)
    print(f'#{tc} {ans}')
