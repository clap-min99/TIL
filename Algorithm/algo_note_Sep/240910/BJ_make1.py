# 1463 1로 만들기

import sys
input = sys.stdin.readline
from collections import deque


def one(N, cnt):
    q = deque([(N, cnt)])
    exist = set()
    exist.add(N)

    while q:
        N, cnt = q.popleft()

        if N == 1:
            return cnt

        if N%3 == 0 and N/3 not in exist:
            exist.add(N/3)
            q.append((N/3, cnt+1))

        if N%2 == 0 and N/2 not in exist:
            exist.add(N/2)
            q.append((N/2, cnt+1))

        if N-1 not in exist:
            exist.add(N-1)
            q.append((N-1, cnt+1))


n = int(input())
ans = one(n, 0)

print(ans)