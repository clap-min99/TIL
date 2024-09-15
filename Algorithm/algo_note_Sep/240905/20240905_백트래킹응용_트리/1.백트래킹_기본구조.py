# 중복 순열

arr = [i for i in range(1, 4)]
visited = [0] * 3


def dfs(level):
    if level == len(arr):
        print(*visited)
        return

    for i in range(len(arr)):
        # 가지치기 : 중복된 숫자 제거
        # if arr[i] in visited:
        #     continue

        visited[level] = arr[i]
        dfs(level + 1)
        # visited[level] = 0


dfs(0)