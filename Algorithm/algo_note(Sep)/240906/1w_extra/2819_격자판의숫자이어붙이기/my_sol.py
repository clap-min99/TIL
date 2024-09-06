import sys
sys.stdin = open('input.txt', 'r')

# 시작점: 각 좌표
# 끝점: 문자열의 길이가 7이면 종료

dij = [[0, 1],[-1, 0],[0, -1],[1, 0]]

def dfs(i, j, path):
    if len(path) == 7:
        result.add(path)
        return

    for di, dj in dij:
        ni = i + di
        nj = j + dj

        if ni <0 or nj<0 or ni >= 4 or nj >= 4:
            continue

        dfs(ni, nj, path + arr[ni][nj])



T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j ,arr[i][j])

    print(f'#{tc} {len(result)}')
