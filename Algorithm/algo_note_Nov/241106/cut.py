# 25305 커트라인
import sys
input = sys.stdin.readline

N, k = map(int, input().split())
score = sorted(map(int, input().split()), reverse=True)
print(score[k-1])
