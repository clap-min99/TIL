# 지뢰찾기
import sys
input = sys.stdin.readline

while True:
    R, C = map(int, input().split())

    if R == 0 and C == 0:
        break

    bomb = [input().strip() for _ in range(R)]

    ans = [[0]*C for _ in range(R)]


    dij = [[1,0],[1,1],[0,1],[1,-1],[-1,0],[-1,1],[-1,-1],[0,-1]]

    for i in range(R):
        for j in range(C):

            if bomb[i][j] == '*':
                ans[i][j] = '*'
                continue

            for di, dj in dij:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= R or nj < 0 or nj >= C:
                    continue
                
                if bomb[ni][nj] == '*':
                    ans[i][j] += 1
    
    for i in range(R):
        for j in range(C):
            print(ans[i][j], end='')
        print()
                    
