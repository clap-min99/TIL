# test
import sys
input = sys.stdin.readline

N = int(input())
ans = 1
for _ in range(N):
    multi = int(input())
    ans += multi-1

print(ans)