import sys
sys.stdin = open('input.txt')

dij = [[1,0],[0,1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = []
    # s = 0
    # for i in range(N):
    #     for j in range(N):
    #         s = arr[i][j]
    #         for di, dj in dij:
    #             ni = i + di
    #             nj = j + dj
    #             if ni == N-1 and nj == N-1:
    #                 break
    #             if 0 <= ni < N and 0 <= nj < N:
    #                 temp.append(arr[ni][nj])
    #             s += min(temp)
    #         temp = []
    # print(s)