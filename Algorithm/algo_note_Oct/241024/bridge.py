# 1010 다리놓기
import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return (n)*factorial(n-1)

t = int(input())
for tc in range(t):
    N, M = map(int, input().split())
    ans = factorial(M)/(factorial(M-N)*factorial(N))
    print(int(ans))
