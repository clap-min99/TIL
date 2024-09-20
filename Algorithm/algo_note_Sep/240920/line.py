N = int(input())
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return (n)*factorial(n-1)

if N == 3:
    print(0)
elif N== 4:
    print(1)    
else:
    ans = factorial(N)/(factorial(N-4)*factorial(4))
    print(int(ans))
