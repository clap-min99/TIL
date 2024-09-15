def frog(pond):
    cur = 0
    while cur < N:
        next = cur + K
        if next >= N:
            return N
        elif pond[next] == 1:
            cur = next
        else:
            found = False
            for i in range(next, cur, -1):
                if pond[i] == 1:
                    cur = i
                    found = True
                    break
            if not found:
                return cur + 1 + K
    return cur + 1 + K            

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pond = list(map(int, input().split()))
    result = frog(pond)
    print(f'#{tc} {result}')