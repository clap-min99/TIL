import sys
input = sys.stdin.readline

burger = [int(input()) for _ in range(3)]
bev = [int(input()) for _ in range(2)]

ans = min(burger) + min(bev) - 50
print(ans)