# 우주선 착륙

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dij = [[0,1],[-1, 1], [-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1]]
    cnt = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            pre_cnt = 0
            for di, dj in dij:
                ni, nj = i +di, j+dj
                if 0<= ni <N and 0 <= nj < M:
                    if s < arr[ni][nj]:
                        pre_cnt += 1
            if pre_cnt >= 4:
                cnt += 1
    print(cnt)

