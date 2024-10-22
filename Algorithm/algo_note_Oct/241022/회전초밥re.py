# 2531 회전초밥
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
# N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

sushi = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):
    dish = set()
    for j in range(k):
        dish.add(sushi[(i+j)%N])        
    if len(dish) < ans:
        continue
    ans = len(dish)
    if c not in dish:
        ans = len(dish) +1

print(ans)
