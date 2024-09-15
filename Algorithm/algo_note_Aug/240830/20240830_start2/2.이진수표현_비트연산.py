def solution():
    mask = (1 << N) - 1
    return (M & mask) == mask


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solution()
    if result:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')