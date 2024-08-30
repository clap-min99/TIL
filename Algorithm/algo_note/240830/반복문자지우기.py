T = int(input())
for tc in range(1, T+1):
    rep = list(input())
    stack = []
    for i in rep:
        if not stack or i != stack[-1]:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
    ans = len(stack)
    print(f'#{tc} {ans}')
