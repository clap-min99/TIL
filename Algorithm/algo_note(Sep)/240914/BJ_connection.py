# 11724 연결요소의 개수
import sys
input = sys.stdin.readline

def dfs(v):        
    visited[v] = 1
    for a in graph[v]:
        if not visited[a]:
            dfs(a)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited =[0]*(N+1)

# graph 만들기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)