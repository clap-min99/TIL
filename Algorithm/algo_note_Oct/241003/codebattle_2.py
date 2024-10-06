tc = int(input())

for tc in range(1, tc+1):
    N, M = map(int, input().split())
    ma = set(input() for _ in range(N))
    sam = set(input() for _ in range(M))
    ans = list(ma&sam)
    ans.sort()
    if ans:
        print(f'#{tc}', *ans)
    else:
        print(f'NO!!')