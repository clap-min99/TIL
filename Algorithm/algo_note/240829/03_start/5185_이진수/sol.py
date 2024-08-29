import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())

    hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}
    ans = []
    for i in range(int(N)):
        ans.append(hex_to_bin[M[i]])
    print(f'#{tc} {"".join(ans)}')
