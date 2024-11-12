# 14503 로봇 청소기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[0]*M for _ in range(N)]
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

visited[r][c] = 1

cnt = 1

dij = [[-1,0],[0,1],[1,0],[0,-1]]

while True:
    flag = 0
    for di, dj in dij:
        ni = r + di*[(d+3)%4]
        nj = c + dj*[(d+3)%4]

        d = (d+3)%4

        if ni < 0 or ni >= N or nj <0 or nj >= M:
            continue

        if room[ni][nj] == 0 and not visited[ni][nj]:
            visited[ni][nj] = 1
            cnt += 1
            r = ni
            c = nj

            flag = 1
            break

    if flag == 0:
        if room[r-di*d][c-dj*d] == 1:
            print(cnt)
        break

    else:
        r, c = r-di*d + c - dj*d