import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = sorted(map(int, input().split()))
    capa = sorted(map(int, input().split()), reverse=True)
    print(capa)
    i = 0
    sum_ = 0
    while True:
        if i == M or not weight:
            break
        a = weight.pop()
        if capa[i] >= a:
            sum_ += a
            i += 1
        elif capa[i] < a:
            continue
    print(f'#{tc} {sum_}')
