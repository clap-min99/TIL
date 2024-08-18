def mock(arr):
    for i in range(N):
        for j in range(N):
            
            for k in range(4):
                cnt = 0
                ni, nj = i, j
              
                while 0<= ni < N and 0<= nj <N and arr[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return('YES')
                    ni += di[k]
                    nj += dj[k]
    return('NO')

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = mock(arr)
    print(f'#{tc} {ans}')
