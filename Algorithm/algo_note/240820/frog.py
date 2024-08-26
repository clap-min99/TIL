T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pond = list(map(int, input().split()))
    cnt = 0
    a = 1
    while cnt < N:
        for i in range(a, a+K):
            cnt += 1
            if pond[i] == 1:
                a = i
                break
    

 

    print(f'#{tc} {cnt}')

    
