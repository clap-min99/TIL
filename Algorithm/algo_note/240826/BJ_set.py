# 11723 집합
import sys
input = sys.stdin.readline

S = set()

M = int(input())

for _ in range(M):
    x = list(map(str, input().split()))
    if x[0] == 'add':
        if int(x[1]) in S:
            continue
        S.add(int(x[1]))
    if x[0] == 'remove':
        if int(x[1]) not in S:
            continue
        S.discard(int(x[1]))
    if x[0] == 'check':
        if int(x[1]) in S:
            print(1)
        if int(x[1]) not in S:
            print(0)
    if x[0] == 'toggle':
        if int(x[1]) in S:
            S.discard(int(x[1]))
        elif int(x[1]) not in S:
            S.add(int(x[1]))
    if x[0] == 'all':
        S = set(i for i in range(1, 21))
    if x[0] == 'empty':
        S = set()