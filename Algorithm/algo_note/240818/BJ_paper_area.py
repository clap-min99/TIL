# 2563 색종이

import sys
input = sys.stdin.readline
N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]

visited =[[0]*100 for _ in range(100)]

for i in range(N):
    for j in range(dot[i][0], dot[i][0]+10):
        for k in range(dot[i][1], dot[i][1]+10):
            visited[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)