# 1920 수 찾기

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    if M_list[i] in N_list:
        print('1')
    else:
        print('0')
