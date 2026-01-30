# https://level.goorm.io/exam/195775/%EC%8B%AC%EB%A6%AC%EC%A0%81-%EA%B1%B0%EB%A6%AC%EA%B0%90/quiz/1
# 

# sol 1 -> 다익스트라는 굳이였다
from heapq import heappush, heappop

N, M, K = map(int, input().split())
bridge = [[] for _ in range(N+1)]

for _ in range(M):
	s, e = map(int, input().split())
	bridge[s].append(e)

# print(bridge)
# 필요한 최소다리의 개수

def dijkstra(start):
	pq = []
	distance = [1e9]*(N+1)
	distance[start] = 0
	# pq에 (누적거리, 현재지점) 나타냄
	heappush(pq, (0, start))
	while pq:
		dist, now = heappop(pq)
		if distance[now] < dist:
			continue

		for next in bridge[now]:
			new_cost = dist + 1

			if new_cost >= distance[next]:
				continue

			distance[next] = new_cost
			heappush(pq, (new_cost, next))
	
	return distance

path = dijkstra(K)
# cal = [[0, 0, 0] for _ in range(N+1)]

max_dis = -1
max_island = -1
for i in range(1, N+1):
	if i == K:
		continue
	if path[i] == 1e9:
		continue
	val = path[i] + abs(K-i)
	if val > max_dis or (val == max_dis and max_island < i):
		max_dis = val
		max_island = i

print(max_island if max_island != -1 else -1)