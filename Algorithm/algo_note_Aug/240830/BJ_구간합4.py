# 11659 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_ = 0
sums = [0]
for i in nums:
    sum_ += i
    sums.append(sum_)       # 누적합을 리스트에 계속 저장

for _ in range(M):
    x, y = map(int, input().split())
    print(sums[y]-sums[x-1])

