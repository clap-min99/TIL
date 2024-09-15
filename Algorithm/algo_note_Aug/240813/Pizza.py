from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
    deq_chz = deque(cheeze)              # 치즈의 양은 뎈으로 저장 
    idx_list = [i for i in range(1, N+1)]   # 인덱스 나타낼 리스트([1,2,3, ...])
    check_list = deque(idx_list[:N])
    left_idx = deque(idx_list[N:])
    pizza = deque(cheeze[:N])    
    leftover = deque(cheeze[N:])
    
    while leftover:
        for c in range(N):
            if pizza.count(0) == N-1:
                break        
            else:
                pizza[0] = pizza[0]//2          # 치즈 반띵
                pizza.rotate(-1)
                check_list.rotate(-1)
                if pizza[0] != 0:               # 치즈가 0이 아니면
                    continue                        
                if pizza[0] == 0:               
                    pizza[0] = leftover.popleft()
                    check_list[0] = left_idx.popleft()                
    
    print(check_list[0])
    
                

            

    

    
    
        
    # for i in range(M):
    #     pizza.append((i+1, cheeze[i]))

    # pizzahut = []
    # for c in range(N):
    #     pizzahut.append(pizza[c][1])

    # print(pizzahut)

    # while True:
    #     for c in range(N):
    #         pizza[c][2] = pizza[c][2]//2

    #         if pizza[c][2] == 0:
                

    #             if not cheeze
    
        