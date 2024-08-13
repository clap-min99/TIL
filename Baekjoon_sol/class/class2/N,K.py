# 11050 이항계수
N, K = map(int, input().split())

def factorial(N):
    if N==1:
        return 1
    f = N*factorial(N-1)
    return f

ans = factorial(N)/(factorial(K)*factorial(N-K))
print(int(ans))