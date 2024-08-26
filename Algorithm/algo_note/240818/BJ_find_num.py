# 1920 수 찾기

N = int(input())
N_list = set(map(int, input().split()))     # 탐색시간을 줄이기 위해 set로 받았다
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)
