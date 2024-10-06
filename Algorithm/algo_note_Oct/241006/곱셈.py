# 1629 곱셈
import sys
input = sys.stdin.readline

def mul(a, b, c):
    if b == 1:
        return a%c
    else:
        k = mul(a, b//2, c)
        if b%2 == 0:
            return (k*k)%c
        else:
            return (k*k*a)%c
        
a, b, c = map(int, input().split())
ans = mul(a,b,c)
print(ans)