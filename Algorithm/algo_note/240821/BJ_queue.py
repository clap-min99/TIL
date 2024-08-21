from collections import deque
import sys
input = sys.stdin.readline
a = deque([])
T = int(input())

for i in range(T):
    q = list(map(str, input().split()))
    if q[0] == 'push':
        a.append(int(q[1]))
    elif q[0] == 'front':
        if not a:
            print(-1)
            continue
        print(a[0])
    elif q[0] == 'back':
        print(a[-1])
    elif q[0] == 'empty':
        if not a:
            print(1)
        if a:
            print(0)
    elif q[0] == 'pop':
        if not a:
            print(-1)
            continue
        print(a.popleft())
    elif q[0] == 'size':
        print(len(a))
    

