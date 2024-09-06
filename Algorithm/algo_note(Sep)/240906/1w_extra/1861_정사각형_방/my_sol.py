import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
dij = [[0, 1],[-1, 0],[0, -1],[1, 0]]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N**2+1)
    for i in range(N):
        for j in range(N):
            for di, dj in dij:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= N or nj <0 or nj >= N:
                    continue

                if arr[ni][nj] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    # 이미 체크 된 순간 다른 방향은 볼 필요가 없다.
                    break

    cnt = max_cnt = start = 0

    for i in range(N*N-1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0

    print(f'#{tc} {start} {max_cnt+1}')