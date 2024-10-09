# 2693 n번째 큰수
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    A = sorted(map(int, input().split()))
    print(A[-3])