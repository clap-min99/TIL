from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s] = e

dist = [1e9]*(N+1)

def bfs(s):
    dist[s] = 0
    q = deque()
    q.append(s)

    while q:
        now = q.popleft()
        
        for nxt in adj[now]:
            if dist[nxt] > dist[now]:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    
    return dist   

best_val = -1
best_island = -1
distance = bfs(K)

for i in range(1,N+1):
    if i == K:
        continue
    if dist[i] == 1e9:
        continue
    
    val = distance[i] + abs(K-i)
    if val > best_val:
        best_val = val
        best_island = i
    if val == best_val and best_island < i:
        best_island = i

if best_val == -1 or not best_val:
    print('-1')
else:
    print(best_island)