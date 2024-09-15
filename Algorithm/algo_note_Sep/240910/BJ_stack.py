import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

nums = [i+1 for i in range(N)]
stack = []
check = 0
i = 0
ans = []
while True:
    if check == N and not stack:
        break

    elif not stack or stack[-1] != arr[check]:
        if i == N:
            ans.append('NO')
            break
        stack.append(nums[i])
        i += 1
        ans.append('+')

    elif stack[-1] == arr[check]:
        stack.pop()
        check += 1
        ans.append('-')

if 'NO' in ans:
    print('NO')
else:
    for pm in ans:
        print(pm)
