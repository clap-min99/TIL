# 14500 테트로미노
import sys
input = sys.stdin.readline

dij = [[0,1],[-1,0],[0,-1],[1,0]]

def dfs(i, j, tmp, cnt):
    global result
    if cnt == 4:
        result = max(result, tmp)
        return
    for di, dj in dij:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if not visited[ni][nj]:
            # 2번째 블록까지 연결했으면
            if cnt == 2:
                visited[ni][nj] = 1
                # 새로운 좌표로 가지 않고 기존 좌표로 돌아와서 탐색('ㅗ','ㅏ')
                dfs(i, j, tmp+arr[ni][nj], cnt+1)
                visited[ni][nj] = 0

            visited[ni][nj] = 1
            dfs(ni, nj, tmp+arr[ni][nj], cnt+1)
            visited[ni][nj] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0
print(result)