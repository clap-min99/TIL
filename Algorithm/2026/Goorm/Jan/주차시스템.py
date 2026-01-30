# 주차시스템
# https://level.goorm.io/exam/152115/%ED%98%84%EB%8C%80%EB%AA%A8%EB%B9%84%EC%8A%A4-%EC%98%88%EC%84%A0-%EC%A3%BC%EC%B0%A8%EC%8B%9C%EC%8A%A4%ED%85%9C/quiz/1
# 성공
from collections import deque

def bfs(i,j):
	q = deque()
	q.append((i,j))
	visited[i][j] = 1
	pre_score = 0
	if parking[i][j] == 2:
		pre_score -= 2
	elif parking[i][j] == 0:
		pre_score += 1
	while q:
		x, y = q.popleft()
		for di, dj in dij:
			dx = x + di
			dy = y + dj

			if dx < 0 or dx >= N or dy < 0 or dy >= M:
				continue
			if not visited[dx][dy] and parking[dx][dy] != 1:
				visited[dx][dy] = 1
				q.append((dx,dy))
				if parking[dx][dy] == 2:
					pre_score -= 2
				elif parking[dx][dy] == 0:
					pre_score += 1
	return pre_score
			

N, M = map(int, input().split())
parking = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# scores = []
dij = [(1,0),(0,1),(-1,0),(0,-1)]
score = 0
for i in range(N):
	for j in range(M):
		if visited[i][j] or parking[i][j] == 1:
			continue
		prv = bfs(i,j)
		if prv > score:
			score = prv
		else:
			continue

print(score)


# 런타임에러
# from collections import deque

# N, M = map(int, input().split())

# parking = [list(map(int, input().split())) for _ in range(N)]

# visited = [[0]*M for _ in range(N)]
# scores = []
# dij = [(1,0),(0,1),(-1,0),(0,-1)]

# for i in range(N):
# 	for j in range(M):
# 		if visited[i][j] or parking[i][j] == 1:
# 			continue

# 		q = deque()
# 		q.append((i,j))
# 		visited[i][j] = 1
# 		score = 0
# 		while q:
# 			x, y = q.popleft()
		
# 			if parking[x][y] == 2:
# 				score -= 2
# 			if parking[x][y] == 0:
# 				score += 1

# 			for di, dj in dij:
# 				dx = x + di
# 				dy = y + dj

# 				if dx < 0 or dx >= N or dy < 0 or dy >= M:
# 					continue
# 				if not visited[dx][dy] and parking[dx][dy] != 1:
# 					q.append((dx,dy))
# 					visited[dx][dy] = 1
# 		scores.append(score)

# ans = 0
# if not scores or max(scores) < 0:
# 	ans = 0
# else:
# 	ans = max(scores)

# print(ans)
				