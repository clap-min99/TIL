# 1026 보물
import sys
input = sys.stdin.readline

N = int(input())
arr1 = sorted(map(int, input().split()))
arr2 = sorted(map(int, input().split()))
arr2.reverse()

ans = 0
for i in range(N):
    ans += arr1[i] * arr2[i]

print(ans)