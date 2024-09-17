import sys
input = sys.stdin.readline

def fibonacci(n):
    global zero_cnt, one_cnt
    if n == 0:
        zero_cnt += 1
        return 0
    elif n == 1:
        one_cnt += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
T = int(input())
for tc in range(T):
    N = int(input())
    zero_cnt = 0   
    one_cnt = 0
    fibonacci(N)
    print(zero_cnt, one_cnt)
