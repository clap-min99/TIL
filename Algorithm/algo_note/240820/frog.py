T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pond = list(map(int, input().split()))
    cnt = 1
    a = 1
    while cnt<N:
        for i in range(a, a+K):
            if pond[i] == 1:
                a = i
                break
            cnt += 1

 

    print(f'#{tc} {cnt}')

    
