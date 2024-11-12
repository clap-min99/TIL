# 1789 수들의 합
import sys
input = sys.stdin.readline
n = int(input())
sum_ = 0
cnt = 0

while True:
    cnt += 1
    sum_ += cnt
    if sum_ > n:
        break

print(cnt-1)