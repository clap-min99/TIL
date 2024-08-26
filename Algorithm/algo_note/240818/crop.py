# 농장물 수확하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    money = 0
    for i in range((N-1)//2 + 1):
        for j in range((N-1)//2-i,(N-1)//2+i+1):
            money += int(farm[i][j])
    for i in range(N//2+1, N):
        for j in range(N//2-(N-i-1), N//2+(N-i)):
            money += int(farm[i][j])
    print(f'#{tc} {money}')