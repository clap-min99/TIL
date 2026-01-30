# 구름_Groom Party
# https://level.goorm.io/exam/352227/goorm-party/quiz/1


# 1. 재귀 사용. recursionlimit 사용해서 억지 해결(?)
# import sys
# sys.setrecursionlimit(300000)

# N, M = map(int, input().split())
# island = [0] + list(map(int, input().split()))
# # print(island)
# # island = [0, 1, 2, 3, 4, 5, .. N]
# bridge = [[] for _ in range(N+1)]


# for _ in range(M):
# 	s , e = map(int, input().split())
# 	bridge[s].append(e)
# 	bridge[e].append(s)

# visited = [0]*(N+1)
# path = []

# def one(c):
# 	path.append(c)
# 	visited[c] = 1

# 	for a in bridge[c]:
# 		if not visited[a]:
# 			one(a)

# one(1)
# ans = 0
# for i in range(1, N+1):
# 	if visited[i]:
# 		ans += island[i]
# print(ans)

# 2 
N, M = map(int, input().split())
island = [0] + list(map(int, input().split()))
# print(island)
bridge = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    bridge[s].append(e)
    bridge[e].append(s)
# print(bridge)
visited = [0]*(N+1)

stack = [1]
visited[1] = 1
ans = 0
while stack:
    print(stack)
    c = stack.pop()
    ans += island[c]
    for i in bridge[c]:
        if not visited[i]:
            visited[i] = 1
            stack.append(i)

print(ans)