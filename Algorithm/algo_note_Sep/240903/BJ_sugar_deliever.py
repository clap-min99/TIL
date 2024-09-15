# 2839 설탕배달
import sys
input = sys.stdin.readline

N = int(input())
M = N           # 반복문 돌 때 초기화 시켜줄 M 값
cnt_lst = []    # 가능한 경우를 더할 리스트
cnt = 0
a = N//3
a_list = [i for i in range(a+1)]    # 3kg가 최대로 있을 수 있는 봉지 개수까지 리스트
a_list.reverse()                    # 그냥 생각하기 편하려고 ... 

for i in range(len(a_list)):        # 3키로로 전부 담는게 최대치니까 그때까지만 돌리면 된다.
    N = N - 3*(a_list[i])           
    cnt += a_list[i]    
    if N == 0:                      # 3키로 최대치로 딱 떨어지면
        cnt_lst.append(cnt)         # 리스트에 담기
        N = M                       # 담았으면 초기화
        cnt = 0                     # cnt도 초기화
    else:
        cnt += N//5                 # 남은 건 5로 나누기
        N = N - 5*(N//5)            # 나눈만큼 빼고
        if N == 0:                  # 나머지가 없으면 담기 
            cnt_lst.append(cnt)
            cnt = 0
            N = M            
        else:                       # 나머지 있으면 정확하게 안떨어지니까,, 
            cnt = 0
            N = M
            continue

if cnt_lst:                 # 리스트에 숫자가 있으면
    print(min(cnt_lst))     # 최솟값 출력
else:                       # 없으면 -1 출력
    print(-1)

