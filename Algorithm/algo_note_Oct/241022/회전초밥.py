# 2531 회전 초밥
import sys
input = sys.stdin.readline
from collections import deque

N, d, k, c = map(int, input().split())
# N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

sushi = deque(int(input()) for _ in range(N))

sushi_set = []

for i in range(N):
    dish = []
    # 회전초밥 돌리면서 0부터 k-1 인덱스 세트 N개 만들기
    su = set(list(sushi)[0:k])
    if su in sushi_set:
        continue
    sushi_set.append(su)
    sushi.rotate(-1)

# 세트의 길이를 기준으로 내림차순 정렬 
sort_sushi = sorted(sushi_set, key = lambda x: -len(x))
max_len = len(sort_sushi[0])
ans = max_len

for i in range(len(sort_sushi)):
    if len(sort_sushi[i]) < max_len:
        continue
    
    # 쿠폰으로 받을 스시가 스시 세트에 없을 떄
    elif c not in sort_sushi[i]: 
        ans += 1
        break

print(ans)

