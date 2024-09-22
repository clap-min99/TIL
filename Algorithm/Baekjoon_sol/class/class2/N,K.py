# 11050 이항계수
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(N):
    if N==0 or N==1:
        return 1
    else:
        return N*factorial(N-1)

print(factorial(N)//(factorial(K)*factorial(N-K)))
