def vir(v):
    visited[v] = 1
    for a in graph[v]:
        if visited[a] == 0:
            vir(a)

N = int(input())
pair = int(input())
graph = [[] for _ in range(N+1)]
for i in range(pair):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(N+1)
vir(1)
print(visited)