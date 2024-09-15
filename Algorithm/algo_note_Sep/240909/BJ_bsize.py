# 7568 덩치
N = int(input())
size = []
for i in range(N):
    x, y = map(int, input().split())
    size.append((x, y))
ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            # 키, 몸무게 둘 다 컸을 때때세어주면 그게 순위가 됨
            cnt += 1
    ans.append(cnt)
print(*ans)



