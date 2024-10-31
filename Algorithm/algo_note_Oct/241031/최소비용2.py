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
    # 누적거리, 현재 지점
    heapq.heappush(pq, (0, start))

    # 거리와 도시를 시작점으로 하는 리스트
    dist_path = [[1e9,[i]] for i in range(n+1) ]

    dist_path[start][0] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dist_path[now][0] < dist:
            continue
        
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist+cost

            if new_cost >= dist_path[next_node][0]:
                continue

            dist_path[next_node][0] = new_cost 
            dist_path[next_node][1] = dist_path[now][1] + [next_node]   
            heapq.heappush(pq, (new_cost, next_node))
    
    return dist_path

low_cost = dijkstra(s)


print(low_cost[e][0])
print(len(low_cost[e][1]))
print(*(low_cost[e][1]))
