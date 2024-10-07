# 15652 N과 M(4)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []

def dfs(start):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)