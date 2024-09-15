import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = deque(int(input()) for _ in range(N))


stack = []
stack.append(arr.popleft())
cnt = 0
i = 0

while len(arr) != 1:
    if len(arr) == 1:
        break
    if stack[0] < arr[i]:        
        # stack[0]는 기준 숫자. arr[i]랑 비교.
        cnt += 1
        stack.pop()
        stack.append(arr.popleft())
        i = 0
        continue
    elif stack[0] >= arr[i]:
        cnt += 1
        i += 1
        if i == len(arr):
            i = 0
            continue
print(arr)
print(cnt)

