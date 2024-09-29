# 2903 중앙 이동 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
dot = 2
for i in range(N):
    dot = dot+2**(i)
ans = dot**2
print(ans)