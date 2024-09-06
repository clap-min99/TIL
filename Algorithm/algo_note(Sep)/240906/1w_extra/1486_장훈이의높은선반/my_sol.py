import sys
sys.stdin = open('input.txt')


def recur(cnt, sum_height):
    global ans
    if sum_height >= B:
        ans = min(ans, sum_height)
        return

    if cnt == N:
        return

    # 기저조건 가지치기, 이미 탑 높이낙 B 이상이라면 더이상 확인할 필요가 없다.


    # cnt 번 점원을 탑에 쌓는다?
    recur(cnt + 1, sum_height + height[cnt])
    # 안쌓는다.
    recur(cnt+1, sum_height)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    # 점원들을 쌓은 탑 중 B에 가장 가까운 높이를 저장
    ans = 1e9 # 10억
    recur(0, 0)
    print(f'#{tc} {ans-B}')


