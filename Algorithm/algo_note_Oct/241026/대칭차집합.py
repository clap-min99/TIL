# 1269 대칭차집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = set(map(int ,input().split()))
B = set(map(int ,input().split()))

A_B = A - B 
B_A = B - A
ans = len(A_B) + len(B_A)
print(ans)