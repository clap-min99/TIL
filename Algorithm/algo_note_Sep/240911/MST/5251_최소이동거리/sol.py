import sys
sys.stdin = open('input.txt')
import heapq


def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[0] = 0

    while q:
        dist, now = heapq.heappop(q)

        for next in graph[now]:
            next, weight = next[0], next[1]
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    distance = [1e9]*(N+1)
    graph = [[] for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e,w])
        graph[e].append([s,w])

    Dijkstra(0)
    print(distance)
    ans = distance[N]
    print(f'#{tc} {ans}')