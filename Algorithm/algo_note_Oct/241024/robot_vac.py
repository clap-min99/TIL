# 14503 로봇청소기
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

# 처음에 로봇청소기가 있는 칸의 좌표(r,c)와 로봇청소기가 바로보는 방향 d
r, c, d = map(int, input().split())

# 0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽
direction = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}

room = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

'''
0은 청소되지 않은 빈칸. 
1은 벽이 있는 것
방의 가장자리 모든 칸에는 벽이 있다. 
로봇청소기가 작동 시작후 작동 멈출 때까지 청소하는 칸의 개수 구하기
'''


def clean(r, c, d):
    q = deque()
    q.append((r,c))

    nr = r + direction[d][0]
    nc = c + direction[d][1]

    
