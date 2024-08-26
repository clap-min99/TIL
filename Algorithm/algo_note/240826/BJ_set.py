# 11723 집합

S = []
S = set(S)
M = int(input())

for _ in range(M):
    x = list(map(str, input().split()))
    if x[0] == 'add':
        S.add(x[1])
    if x[0] == 'remove':
        S.remove(x[1])
    if x[0] == 'check':
        if x[1] in S:
            print(1)
        if x[1] not in S:
            print(0)
    if x[0] == 'toggle':
        if x[1] in S:
            S.remove(x[1])
        if x[1] not in S:
            S.add(x[1])
    if x[0] == 'all':
        S = set(i for i in range(1, 21))
    if x[0] == 'empty':
        S = {}
    