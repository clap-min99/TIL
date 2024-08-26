N_pole = 1
S_pole = 2
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0     # 교착상태 개수
    for j in range(N):        # 열 우선 순회
        np = 0                # 아래로 향하는 N극이 있는지 표시
        for i in range(N):
            if arr[i][j] == N_pole:
                np = 1
            elif arr[i][j] == S_pole and np == 1:   # 교착 상태 발생
                cnt += 1
                np = 0
    print(f'#{tc} {cnt}')
