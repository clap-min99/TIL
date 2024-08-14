T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []

    for r in range(N-M+1):
        for s in range(N-M+1):
            sum_fly = 0
            for i in range(r, r+M):
                for j in range(s, s+M):
                    sum_fly += arr[i][j]
            result.append(sum_fly)
    
    print(f'#{tc} {max(result)}')
