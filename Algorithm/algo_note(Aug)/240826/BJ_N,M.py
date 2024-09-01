# 15649 백준 N과 M(backtracking)

import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if v[j] == 0:       # 선택하지 않은 숫자인 경우 추가
            v[j] = 1        
            dfs(n+1, lst+[j])   
            v[j] = 0        # 더해줬으면(?) 0으로 돌려주기

N, M = map(int, input().split())
ans = []
v = [0]*(N+1)   # 중복확인을 위한 visited

dfs(0, [])
for lst in ans:
    print(*lst)
