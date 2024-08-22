T = 10
for tc in range(1, T+1):
    N, pw = input().split()
    stack = ['a']
    pw_list = []
    for i in pw:
        pw_list.append(i)
    for i in range(int(N)):
        if stack[-1] != pw_list[i]:
            stack.append(pw_list[i])
        else:
            stack.pop()
    stack.pop(0)
    
    print(f'#{tc} {"".join(stack)}')

