T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 노선 수
    bus_len = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

    bus_cnt = [0] * P

    for i in range(P):
        for j in range(N):
            if bus_len[j][0] <= bus_stop[i] <= bus_len[j][1]:
                bus_cnt[i] += 1

    print(f'#{tc}', *bus_cnt)
