# 9095 1,2,3 더하기
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N = int(input())
    ans = 0

    a = 1
    b = 2
    c = 4
    if N == 1:
        ans = a
    elif N == 2:
        ans = b
    elif N == 3:
        ans = c
    else:
        for i in range(N-3):
            ans = a + b + c
            a = b
            b = c
            c = ans
    print(ans)