import sys
sys.stdin = open('input.txt')
import heapq


def prim(start):
    q =[]
    visited = [0]*(V+1)
    result = 0      # 최소 누적합 저장

    heapq.heappush(q, (0, start))

    while q:
        weight, now = heapq.heappop(q)
        if not visited[now]:
            visited[now] = 1
            result += weight
            for next in range(V+1):
                if graph[now][next] and not visited[next]:
                    heapq.heappush(q, (graph[now][next], next))
    return result


T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())

    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        x, y, w = map(int, input().split())
        graph[x][y] = w
        graph[y][x] = w

    ans = prim(0)
    print(f'#{tc} {ans}')
