T = 10
for tc in range(1, T+1):
    N = int(input())
    nums = list(input())
    stack = []

    for i in nums:
        if i.isdigit():
            stack.append(i)
            if len(stack) == 2:
                ans = int(stack[-1] + stack[-2])
                stack.pop()
                stack.pop()
                stack.append(ans)
    print(f'#{tc} {ans}')