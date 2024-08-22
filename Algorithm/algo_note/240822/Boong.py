T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    boongs = sorted(map(int, input().split()))
    b_cnt = 0
    ans = 'possible'
    for arv in boongs:
        b_cnt += 1
        if (arv//M)*K < b_cnt:
            ans = 'impossible'
    print(f'#{tc} {ans}')