def solution():
    tar = M
    # 1비트씩 우측으로 옮기면서 같은 지 체크
    for i in range(N):
        if tar & 0x1 == 0:
            return False
        tar = tar >> 1
    return True

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solution()
    if result:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')