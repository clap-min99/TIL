import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

sum_lst = []
for i in range(N):
    for j in range(M):
        x = A[i][j] + B[i][j]
        sum_lst.append(x)
    print(*sum_lst)
    sum_lst = []