import sys
input = sys.stdin.readline

X = int(input())
poll = [2**i for i in range(6, -1 , -1)]
cnt = 0

for i in poll:
    while X-i>= 0:
        X -= i
        cnt += 1
print(cnt)