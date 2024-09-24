# 11403 경로 찾기
# import sys
# input = sys.stdin.readline
# from collections import deque

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]

# def dfs(x):
#     for i in range(N):
#         if graph[x][i] == 1 and visited[x][i] == 0:
#             visited[x][i] = 1
#             dfs(i)

# for i in range(N):
#     dfs(i)
# print(visited)
# ㅠㅠ