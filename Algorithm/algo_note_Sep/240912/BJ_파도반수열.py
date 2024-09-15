# 9461 파도반 수열
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    P = [0, 1, 1, 1, 2]
    if N >= 5:
        for i in range(5, N+1):
            num = P[i-1] + P[i-5]
            P.append(num)
    print(P[N])
