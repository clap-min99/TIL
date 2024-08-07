T = int(input())

for tc in range(1, T + 1):
    N, M = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    result = []
    for x in range(N):
        for y in range(M):
            s = arr[x][y]               # x,y 좌표에 있는 꽃가루 개수
            for dx, dy in dxy:
                for i in range(1, s+1):
                    nx = x + i*dx
                    ny = y + i*dy
                    if 0 <= nx < N and 0 <= ny < M:
                        s += arr[nx][ny]
            result.append(s)
    print(f'#{tc} {max(result)}')
