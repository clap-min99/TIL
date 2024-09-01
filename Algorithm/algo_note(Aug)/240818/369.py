# 간단한 369 게임
N = int(input())
n_list = []
for i in range(1,N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
        print(f'{"-"*cnt}', end = ' ')
    else:
        print(i, end = ' ')