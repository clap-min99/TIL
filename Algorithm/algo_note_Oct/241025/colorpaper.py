# 2630 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

w = 0
b = 0

def colorpaper(N):
    # 확인 할 시작 값
    start = [[0,0], [0,N/2-1], [N/2-1,0], [N/2-1, N/2-1]]

    for i in start:
        for j in range(N/2):
            for k in range(N/2):
                
                paper[i+j][i+k]