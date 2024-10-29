# 11404 플로이드
import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
cost = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):

    pq = []
    # 누적거리, 현재 지점
    heapq.heappush(pq, (0, start))

    distance = [1e9]*(n+1)

    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue
        
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist+cost

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost    
            heapq.heappush(pq, (new_cost, next_node))
    
    return distance

for i in range(1,n+1):
    arr = dijkstra(i)
    for j in range(1, n+1):
        if arr[j] == 1e9:
            arr[j] = 0        
    print(*arr[1:])