# import sys
# sys.stdin = open('sample_input (2).txt')
dij = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc}', end=' ')
    ans = []
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            coord = []
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N:  # 범위 벗어나는 거 제외
                    continue
                if s == '.':                                # .로 시작하는거 제외
                    continue
                if arr[ni][nj] == 'o':            # 기준점 주위에 o가 있는 방향을 저장하는 리스트 생성
                    coord.append([di, dj])

                for x in range(len(coord)):
                    y =1

                    while y != 6:
                        ni = i + y * coord[x][0]  # coord[x][0]은 검사하고자 하는 방향의 di값
                        nj = j + y * coord[x][1]  # coord[x][1] 검사하고자 하는 방향의 dj값
                        if y == 5:
                            ans.append(1)
                            break
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:  # 범위 벗어나는 거 제외
                            break
                        if arr[ni][nj] == '.':
                            break
                        if arr[ni][nj] == 'o':
                            y += 1
    if ans:
        print('YES')
    if not ans:
        print('NO')

