# 2531 회전초밥
import sys
input = sys.stdin.readline
from collections import deque

N, d, k, c = map(int, input().split())
# N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

sushi = deque(int(input()) for _ in range(N))

ans = 0

for i in range(N):
    # 초밥 회전시키면서 k만큼 인덱싱.
    # 서비스 초밥 더해주고 set로 만듦
    dish = set(list(sushi)[0:k]+[c])
    sushi.rotate(-1)
    # 현재 가짓수가 지금까지의 최대 가짓수보다 작으면 continue
    if len(dish) < ans:
        continue
    # 현재 가짓수가 최대 가짓수가 되면 종료
    if len(dish) == k+1:
        ans = k+1
        break
    ans = len(dish)

print(ans)
