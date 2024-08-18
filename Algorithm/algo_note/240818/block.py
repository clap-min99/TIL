T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    block = sorted(map(int, input().split()))
    block_2 = []
    if M1 <= M2:
        for i in range(N-1, N-(2*M1+1),-2):
            block_2.append(block.pop(i-1))
        sum_block = 0
        for x in range(M1):
            sum_block += (x+1)*block_2[x]  # append 해서 내림차순 정렬 되어있음
        
        for y in range(M2):
            sum_block += (y+1)*block[-(y+1)]    # 원래 리스트는 오름차순 정렬
   
    if M1 > M2:
        for i in range(N-1, N-(2*M2+1),-2):
            block_2.append(block.pop(i))
        sum_block = 0
        for x in range(M2):
            sum_block += (x+1)*block_2[x]  # append 해서 내림차순 정렬 되어있음
        
        for y in range(M1):
            sum_block += (y+1)*block[-(y+1)]    # 원래 리스트는 오름차순 정렬
    print(f'#{tc} {sum_block}')
