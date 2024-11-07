# 18528 큐2
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

cmds = []
for i in range(N):
    cmd = list(input().split())
    cmds.append(cmd)

    if cmds[i][0] == 'push':
        q.append(int(cmds[i][1]))
    
    if cmds[i][0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    
    if cmds[i][0] == 'size':
        print(len(q))

    if cmds[i][0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    
    if cmds[i][0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    if cmds[i][0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
    