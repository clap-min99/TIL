# 7785 회사에 있는 사람
import sys
input = sys.stdin.readline

n = int(input())

working = set()

for _ in range(n):
    name, log = map(str, input().split())

    if log == 'enter':
        working.add(name)
        
    elif log == 'leave':
        working.remove(name)

ans = sorted(working, reverse=True)

for i in range(len(ans)):
    print(ans[i])