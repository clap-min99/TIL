# 1504 특정한 최단 경로
import sys
input = sys.stdin.readline
import heapq

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

distance = [1e9]*(N+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 두개의 정점
v1,v2 = map(int, input().split())

def dijiktra(start):
    pq = []
    heapq.heappush(pq, (0, start))

    