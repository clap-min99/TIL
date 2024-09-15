N , K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

coin.reverse()
cnt = 0
for i in range(N):
    if K//coin[i] == 0:
        continue
    cnt += K//coin[i]
    K = K%coin[i]    
print(cnt)
