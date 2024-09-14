# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in (1, T+1):
    num, ch_ = input().split()
    switch = int(ch_)   # 교환횟수는 숫자로
    N = len(num)
    nums = [num[i] for i in range(N)]    # 숫자판 정보는 리스트에 하나씩
