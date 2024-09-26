# 11403 경로찾기
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# path = []

# # 경로 만들기
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1:
#             path.append((i,j))



def find(a, start):
    for i in range(N):        
        if graph[start][i] == 1 and not visited[a][i]:
            visited[a][i] = 1
            find(a, i)

for i in range(N):
    find(i, i)

for i in visited:
    print(*i)