# 1316 그룹 단어 체커 

import sys
input = sys.stdin.readline

N = int(input())

words = [list(input())[:-1] for _ in range(N)]
cnt = N
for i in range(N):
    for j in range(len(words[i])-1):
        if words[i][j] == words[i][j+1]:
            continue
        elif words[i][j] in words[i][j+1:]:
            cnt -= 1
            break
print(cnt)