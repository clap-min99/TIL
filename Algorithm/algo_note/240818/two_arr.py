T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N < M:
        ans = []
        for i in range(M-N+1):
            p_sum = 0
            for j in range(N):
                p_sum += A[j]*B[j+i]
            ans.append(p_sum)
    if M < N:
        ans = []
        for i in range(N-M+1):
            p_sum = 0
            for j in range(M):
                p_sum += B[j]*A[j+i]
            ans.append(p_sum)
    if M == N:
        ans = []
        p_sum = 0
        for i in range(N):
            p_sum += A[i]*B[i]
        ans.append(p_sum)
    
    print(f'#{tc} {max(ans)}')
    