# 1753 최단경로
import sys
input = sys.stdin.readline
import heapq

# 간선, 노드
V, E = map(int, input().split())

# K는 시작정점
K = int(input())


# 인접리스트(노드의 개수 만큼)
graph = [[] for _ in range(V+1)]

# 누적거리 저장할 테이블
INF = 1e9
distance = [INF]*(V+1)

for _ in range(E):
    # u에서 v로 가는 가중치 w인 간선
    u, v, w = map(int, input().split())
    graph[u].append([v,w])

def dijkstra(start):
    q = []

    # q에 시작 지점, 최단거리 push
    heapq.heappush(q, (0, start))
    
    # 시작지점에서의 누적 거리 0 
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드에 대한 누적 거리가 이미 처리되었다면
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 인접 노드 확인하기
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # 가중치 더하기
            new_cost = dist + cost

            # 다음 노드를 가는 데 더 많은 비용이 들면
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])