import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_t = []
    for _ in range(N):
        s, e = map(int, input().split())
        work_t.append((s, e))
    work = sorted(work_t, key=lambda x: x[1])
    print(work)
    ans = 1
    cur = 0
    comp = 1
    for _ in range(N-1):
        if work[cur][1] <= work[cur+comp][0]:
            cur = cur + comp
            comp = 1
            ans += 1
        else:
            comp += 1
    print(f'#{tc} {ans}')



