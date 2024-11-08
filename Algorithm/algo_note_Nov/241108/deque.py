# 28279 deque2
import sys
input = sys.stdin.readline
from collections import deque

q = deque()

cmds = []
N = int(input())
for i in range(N):
    cmd = list(input().split())
    cmds.append(cmd)

    if cmds[i][0] == '1':
        q.append(int(cmds[i][1]))
        q.rotate(1)
    elif cmds[i][0] == '2':
        q.append(int(cmds[i][1]))
    elif cmds[i][0] == '3':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmds[i][0] == '4': 
        if q:
            print(q.pop())
        else:
            print(-1)
    elif cmds[i][0] == '5':
        print(len(q))
    elif cmds[i][0] == '6':
        if q:
            print(0)
        else:
            print(1)
    elif cmds[i][0] == '7':
        if q:
            print(q[0])
        else:
            print(-1)

    elif cmds[i][0] == '8':
        if q:
            print(q[-1])
        else:
            print(-1)