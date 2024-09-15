# swea
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def DFS(s, N):              # s 시작정점,N 정점개수
    stack = []              # stack 생성
    visited[s] = 1          # 시작점 표시
    v = s                   # v는 현재 위치 표시
    result = [v]
    while True:
        for w in adjL[v]:       # adjL은 빈 리스트의 리스트?
            if visited[w] == 0:     # 방문한 적이 없으면
                stack.append(v)     # 현재 정점(위치) push
                visited[w] = 1      # 방문표시
                v = w               # w에 방문
                result.append(v)
                break               # for w, v부터 다시 탐색
        else:                       # for else: for문을 전부 돌았을 경우 실행
            if stack:               # stack에 탐색할 갈림길이 남아있으면?
                v = stack.pop()
            else:
                break
    return result


T = 1
for tc in range(1, T + 1):
    N, E = map(int, input().split())    # N은 정점 개수
    arr = list(map(int, input().split()))
    visited = [0]*(N+1)
    adjL = [[] for _ in range(N + 1)]  # 인접리스트 초기화
    s = 1
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2 + 1]
        # arr의 짝수 번째에는 정점, 홀수 번째에는 정점과 연결되어 있는 점 표시
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    result = DFS(s, N)
    print(f'#{T} {"-".join(map(str, result))}')