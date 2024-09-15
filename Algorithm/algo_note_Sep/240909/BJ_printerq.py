# 1966 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    im = deque(map(int, input().split()))
    result = 1
    while im:
        if im[0] < max(im):
            im.rotate(-1)

        else:
            if M == 0:
                break
            im.popleft()
            result += 1

        if M > 0:
            M = M - 1
        else:
            M = len(im) -1
    print(result)


