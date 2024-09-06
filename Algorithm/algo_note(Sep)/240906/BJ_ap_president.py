# 2775 부녀회장이 될테야

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())

    build = [[1] for i in range(16)]
    for i in range(2, 15):
        build[0].append(i)

    for i in range(1, k+1):
        for j in range(1, n):
            people = build[i-1][j] + build[i][j-1]
            build[i].append(people)
    print(build[k][n-1])

