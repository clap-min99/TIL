from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    rot_num = deque(map(int, input().split()))

    for i in range(M):
        rot_num.rotate(-1)
    
    ans = list(rot_num)

    print(f'#{tc} {ans[0]}')


