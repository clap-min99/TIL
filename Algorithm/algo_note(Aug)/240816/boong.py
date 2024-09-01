T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명의 사람, M초에 K개의 붕어빵
    ar_time = list(map(int, input().split()))   # 손님이 도착하는 시ㅏㄱㄴ
    print(f'#{tc}', end=' ')
    cnt_bng = 0
    for i in range(N):
        cnt_bng = (ar_time[i]//M)*K
        cnt_bng -= 1
    if not cnt_bng:
        print('Impossible')
    else:
        if cnt_bng:
            print('Possible')
