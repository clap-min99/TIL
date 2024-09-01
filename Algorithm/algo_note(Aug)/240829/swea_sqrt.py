# 5688 세제곱근을 찾아라

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tst = int(N**(1/3))
    ans = -1
    for i in range(tst-2, tst+2):
        if i**3 == N:
            ans = i
    print(f'#{tc} {ans}')