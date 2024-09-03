# 2839 설탕배달

N = int(input())
M = N
cnt_lst = []
cnt = 0
a = N//3
b = N//5
a_list = [i for i in range(a+1)]
b_list = [i for i in range(b+1)]
a_list.reverse()

for i in range(len(a_list)):
    N = N - 3*(a_list[i])
    cnt += a_list[i]    
    if N == 0:
        cnt_lst.append(cnt)
        N = M
        cnt = 0
    else:
        cnt += N//5
        N = N - 5*(N//5) 
        if N == 0:
            cnt_lst.append(cnt)
            cnt = 0
            N = M            
        else:
            cnt = 0
            N = M
            continue

if cnt_lst:
    print(min(cnt_lst))
else:
    print(-1)

