def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

N = int(input())
cnt = 0
f_num = str(factorial(N))
for i in range(len(f_num)-1, 0, -1):
    if f_num[i] == '0':
        cnt += 1
    elif f_num[i] != '0':
        break
print(cnt)