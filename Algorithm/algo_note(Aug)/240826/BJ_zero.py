# 10773 제로
import sys
input = sys.stdin.readline
K = int(input())
zero = []
for i in range(K):
    a = int(input())
    if a != 0:
        zero.append(a)
    elif a == 0:
        zero.pop()
ans = sum(zero)
print(ans)