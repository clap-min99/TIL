def check(row):
    for col in range(row):
        if visited[row] == visited[col]:
            return False

        # 열과 행의 차이가 같다 == 현재 col 의 좌우 대각선이다
        if abs(visited[row] - visited[col]) == abs(row - col):
            return False

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col
        if not check(row):
            continue

        dfs(row + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * N
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')