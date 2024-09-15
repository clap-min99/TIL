T = int(input())
dij = [[0, 1], [-1, 0], [0, -1], [1, 0]]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_lst = []
    for i in range(N):
        sum_ = 0
        for j in range(N):
            s = arr[i][j]
            for a in range(M//2+1):
                for b in range(M//2-a, M//2+a+1):
                    if 0 <= i+a < N and 0 <= j+b < N:
                        sum_ += arr[i+a][j+b]

            sum_lst.append(sum_)






