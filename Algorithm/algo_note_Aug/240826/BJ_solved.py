import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = sorted(int(input()) for _ in range(n))
a = int(n*0.15+0.5)
dq_arr = deque(arr)

for _ in range(a):
    dq_arr.pop()
    dq_arr.popleft()

arr = list(dq_arr)
if len(arr) == 0:
    ans = 0
else:
    ans = int((sum(arr)/len(arr))+0.5)
print(ans)

# 사사오입, 오사오입
# Python의 round 함수는 오사오입, 즉 5미만은 내리고 5초과는 올리는 방식이다.
# 사사오입 반올림(4 이하는 내리고 5 이상은 올림)이 아님에 유의하자.
# 이 문제에서는 강제로 0.5 더해서 int처리로 반올림(?) 해줬다.
