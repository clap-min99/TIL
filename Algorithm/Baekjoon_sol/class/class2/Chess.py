#1018 체스판 다시 칠하기

N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]
result = []

for i in range(N-7):
    for j in range(M-7):
        bl_cnt = 0
        wh_cnt = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'B':
                        bl_cnt += 1
                    if arr[a][b] != 'W':
                        wh_cnt += 1
                else:
                    if arr[a][b] != 'W':
                        bl_cnt += 1
                    if arr[a][b] != 'B':
                        wh_cnt += 1

        result.append(bl_cnt)
        result.append(wh_cnt)

print(min(result))






