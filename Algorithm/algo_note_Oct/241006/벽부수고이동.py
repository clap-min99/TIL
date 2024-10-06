# 2206 벽 부수고 이동하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]
