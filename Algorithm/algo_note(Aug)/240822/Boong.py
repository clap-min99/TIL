T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    boongs = sorted(map(int, input().split()))
    b_cnt = 0
    ans = 'Possible'
    for arv in boongs:
        b_cnt += 1
        if (arv//M)*K < b_cnt:
            ans = 'Impossible'
    print(f'#{tc} {ans}')