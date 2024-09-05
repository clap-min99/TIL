# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
arr = [i for i in range(1, 11)]
visited = []


def dfs(level, sum):
    if level == len(arr):
        return

    if sum > 10:
        return

    if sum == 10:
        print(*visited)
        return

    for i in range(len(arr)):
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i])
        visited.pop()


dfs(0, 0)