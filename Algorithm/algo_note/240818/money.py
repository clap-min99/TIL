# 쉬운 거스름돈
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt_list = []
    for i in range(8):
        cnt_list.append(str(N // money[i]))
        N -= money[i]*(N//money[i])
    print(f'#{tc}') 
    print(*cnt_list)