# 1916 최소비용 구하기

import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

s, e = map(int, input().split())

distance = [1e9]*(N+1)

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = cost+dist

            if new_cost >= distance[next_node]:
                continue
            
            distance[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))

dijkstra(s)
print(distance[e])