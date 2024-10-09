# 13549 숨바꼭질 3
import sys
input = sys.stdin.readline
from collections import deque


def find(s, cnt):
    q = deque()
    q.append((s, cnt))
    visited = set()
    visited.add(s)

    while q:
        n, cnt = q.popleft()
        if n == K:
            return cnt
        
        if n*2 not in visited and -1< n*2 < limit:
            q.append((n*2, cnt))
            visited.add(n*2)
        
        if n-1 not in visited and -1< n-1 < limit:
            q.append((n-1, cnt+1))
            visited.add(n-1)

        if n+1 not in visited and -1< n+1 < limit:
            q.append((n+1, cnt+1))
            visited.add(n+1)
        
    
N, K = map(int, input().split())
limit = 100001
ans = find(N, 0)
print(ans)