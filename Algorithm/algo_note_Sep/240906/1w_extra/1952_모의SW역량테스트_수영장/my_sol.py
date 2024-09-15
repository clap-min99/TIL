import sys
sys.stdin = open('input.txt')


def dfs(n, acc):
    global result
    if acc > result:        # 누적합이 더 크면 되돌리기
        return

    if n >= 12:             # 일년치 계산 끝
        if acc < result:    # 누적합이 더 작으면
            result = acc    # 작은 값으로 갱신

    else:
        if plan[n]:
            # day로 계산
            dfs(n+1, acc + fee[0]*plan[n])
            # month로 계산
            dfs(n+1, acc + fee[1])
            # 3 month로 계산
            dfs(n+3, acc + fee[2])
        else:
            dfs(n+1, acc)


T = int(input())
for tc in range(1, T+1):
    fee = list(map(int, input().split()))   # 1일, 한 달, 세 달, 일년
    plan = list(map(int, input().split()))  # 수영 계획
    result = fee[3]    # 큰 값
    dfs(0, 0)
    print(f'#{tc} {result}')