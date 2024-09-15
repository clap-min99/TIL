T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    len_arr = []
    for i in range(N):
        len_arr.append(len(arr[i]))
    
    R = max(len_arr)
    
    

    for i in range(R):
        for j in range(M):
            pass

    # if N<M:
    #     print(f'#{tc}, -1')
    