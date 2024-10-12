# 16953 A->B
import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int, input().split())
q = deque()
cnt = 0
q.append((A, cnt))
# visited = [0]*(10**9)


def change(A):
    q = deque()
    cnt = 1
    q.append((A, cnt))

    while q:
        a, cnt = q.popleft()

        if a == B:
            return cnt
        
        if a*2 <= B:
            # visited[a*2] = 1
            q.append((a*2, cnt+1))
        
        if a*10 +1 <= B:
            q.append((a*10+1, cnt+1))
    
    return(-1)
    
ans = change(A)
print(ans)