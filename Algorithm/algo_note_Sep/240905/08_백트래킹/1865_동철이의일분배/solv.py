def max_success(now, comp):
    global result
    if result >= comp:
        return

    if now == N:
        result = max(result, comp)

    else:
        for w in range(N):
            if not visited[w]:
                visited[w] = 1
                max_success(now+1, comp*(percent_list[now][w]/100))
                visited[w] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent_list = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 0
    max_success(0, 1)
