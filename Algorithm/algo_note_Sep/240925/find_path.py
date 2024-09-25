# 11403 경로찾기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
path = []

# 경로 만들기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            path.append((i,j))


adj_l = [[0]*N for _ in range(N)]

print(path)



def find():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                