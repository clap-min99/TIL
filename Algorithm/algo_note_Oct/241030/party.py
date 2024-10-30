# 1238 파티
import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(start):
    pq = []

    heapq.heappush(pq, (0, start))

    distance = [1e9]*(N+1)

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = cost+dist

            if new_cost >= distance[next_node]:
                continue
            
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

    return distance

dist_list = []
for i in range(1, N+1):
    arr = dijkstra(i)
    dist_list.append(int(arr[X]))
print(dist_list)