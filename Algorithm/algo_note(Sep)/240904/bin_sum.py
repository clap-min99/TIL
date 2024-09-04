# 1252 이진수 덧셈

A, B = input().split()
ans = bin(int(A, 2)+int(B, 2))[2:]
print(ans)