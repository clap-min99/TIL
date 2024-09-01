# 2231 분해합
N = int(input())

for i in range(N):
    result = sum(int(x) for x in str(i))
    result += i
    if result == N:
        print(i)
        break
else:
    print(0)