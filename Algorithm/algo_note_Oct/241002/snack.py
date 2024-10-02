# 10156 과자

import sys
input = sys.stdin.readline

K, N, M = map(int, input().split())

ans = K*N -M

if ans <= 0:
    ans = 0
else:
    ans = ans
print(ans)