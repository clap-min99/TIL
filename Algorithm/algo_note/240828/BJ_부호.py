# 1247 부호
import sys
input = sys.stdin.readline
T = 3
for tc in range(1, T+1):
    N = int(input())
    sum_lst = [int(input()) for _ in range(N)]
    if sum(sum_lst) > 0:
        print('+')
    elif sum(sum_lst) == 0:
        print('0')
    elif sum(sum_lst) < 0:
        print('-')
