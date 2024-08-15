T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dij = [[0,1],[1,0],[0,-1],[-1,0]]
    result = []

    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if 0<= ni < N and 0<= nj<M:
                    s += arr[ni][nj]
                result.append(s)
    print(f'#{tc} {max(result)}')


        
