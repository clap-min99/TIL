import sys
sys.stdin = open('input.txt')
from collections import deque


def cal(n, cnt):
    q = deque([(n, cnt)])
    visited = set()     # 같은 결과값 나왔으면 굳이 연산 더 할 필요가 없다.
    visited.add(n)

    while q:
        n, cnt = q.popleft()

        if n == M:
            return cnt

        if n*2 not in visited and n*2 <= 10**6:
            q.append((n*2, cnt+1))
            visited.add(n * 2)

        if n+1 not in visited and n+1 <= 10**6:
            q.append((n+1, cnt+1))
            visited.add(n + 1)

        if n-1 not in visited and n-1 <= 10**6:
            q.append((n-1, cnt+1))
            visited.add(n - 1)

        if n-10 not in visited and n-10 <= 10**6:
            q.append((n-10, cnt+1))
            visited.add(n - 10)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = cal(N, 0)
    print(f'#{tc} {ans}')
