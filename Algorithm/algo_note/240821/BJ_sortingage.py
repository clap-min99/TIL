import sys
input = sys.stdin.readline

N = int(input())

user = [tuple(input().split()) for _ in range(N)]

for i in sorted(user, key = lambda x: int(x[0])):
    print(i[0],i[1])