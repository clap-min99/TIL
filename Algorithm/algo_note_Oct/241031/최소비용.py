# 11779 최소비용 구하기 2

import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

s,e = map(int, input().split())

def dijkstra(start):

    pq = []

    heapq.heappush(pq, (0, start))

    distance = [1e9]*(n+1)

    distance[start] = 0

    
    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = next[1]
            next_node = next[0]

            new_cost = dist+cost

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            
            heapq.heappush(pq, (new_cost, next_node))
    return distance

low_cost = dijkstra(s)

