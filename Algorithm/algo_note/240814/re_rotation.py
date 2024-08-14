from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = deque(map(int, input().split()))
    for i in range(M):
        nums.rotate(-1)
    print(f'#{tc} {nums[0]}')
