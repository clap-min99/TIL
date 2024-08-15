T = int(input())

for tc in range(1, T+1):
    c_num = int(input())
    c_size = list(map(int, input().split()))

    result = []
    cnt = 1
    a = 0
    for a in range(c_num-1):       
        if c_size[a] < c_size[a+1]:     # 당근이 커진 경우
            cnt += 1           
            if a == c_num-2:
                result.append(cnt)
                
        if c_size[a] >= c_size[a+1]:    # 다음 당근이 작거나 크기가 같은 경우
            result.append(cnt)
            cnt = 1                     # 1로 초기화      
            if a == c_num-2:
                result.append(cnt)
                
    print(f'#{tc} {max(result)}')
        