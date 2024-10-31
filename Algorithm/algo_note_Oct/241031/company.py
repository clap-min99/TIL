# 7785 회사에 있는 사람
import sys
input = sys.stdin.readline

n = int(input())

working = set()
leaving = set()
for _ in range(n):
    name, log = map(str, input().split())

    if log == 'enter':
        working.add(name)
        

    elif log == 'leave':
        leaving.add(name)

ans = sorted(working - leaving)



for i in range(len(ans)):
    print(ans[len(ans)-i-1])