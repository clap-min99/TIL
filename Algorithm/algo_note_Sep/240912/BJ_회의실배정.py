# 1931 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
conf = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
conference = sorted(conf, key=lambda x: (x[1], x[0]))
a = 0
comp = 1
while True:
    if a + comp == N:
        break
    if conference[a][1] <= conference[a+comp][0]:
        cnt += 1
        a = a+comp
        comp = 1
    else:
        comp += 1

print(cnt)