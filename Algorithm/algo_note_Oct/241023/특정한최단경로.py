# 1504 특정한 최단 경로
import sys
input = sys.stdin.readline
import heapq

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]



for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 반드시 거쳐야 하는 두개의 정점 v1,v2
v1,v2 = map(int, input().split())

def dijkstra(start):
    pq = []
    distance = [1e9]*(N+1)
    heapq.heappush(pq, (0, start))

    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        # now에 방문한적 있으면,, (방문안한 distance는 INF로 만들어놨따)
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = cost + dist
            
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))       
    
    # 최단거리 '배열' 반환
    return distance

# 1부터 출발 최단 거리 배열 
shortest_path = dijkstra(1)
# v1 시작 최단 거리 배열
v1_start = dijkstra(v1)
# v2 시작 최단 거리 배열
v2_start = dijkstra(v2)

# 1-> v1 -> v2 -> v
way1 = shortest_path[v1] + v1_start[v2] + v2_start[N]

# 1-> v2 -> v1 -> v
way2 = shortest_path[v2] + v2_start[v1] + v1_start[N]

ans = min(way1, way2)

if ans < 1e9:
    print(ans)
else:
    print(-1)