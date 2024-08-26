# 직사각형 4개의 합집합 면적 구하기
dot = [list(map(int, input().split())) for _ in range(4)]

visited =[[0]*100 for _ in range(100)]

for i in range(4):
    for j in range(dot[i][0], dot[i][2]):
        for k in range(dot[i][1], dot[i][3]):
            visited[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)


