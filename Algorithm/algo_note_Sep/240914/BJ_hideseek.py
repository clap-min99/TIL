# 1697 숨바꼭질

import sys
input = sys.stdin.readline
from collections import deque


def seek(n):
    q = deque()
    q.append(n)
    while q:
        cur = q.popleft()
        if cur == K:
            return visited[K]
        for i in (cur+1, cur-1, 2*cur):
            if 0<= i <= 100000 and not visited[i]:
                visited[i] = visited[cur]+1
                q.append(i)

visited = [0]*(100001)
N, K = map(int, input().split())
print(seek(N))
