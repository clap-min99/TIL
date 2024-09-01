T = int(input())
stack = []
cal_dict = {'+': 1, '-': 1, '*': 2, '/': 2}

for tc in range(1, T+1):

    stack = []
    ans = []
    read = input()
    for i in read:
        if i.isdecimal():
            ans.append(i)
        else:
            if i == '+' or i == '-':
                while stack:
                    ans.append(stack.pop())
                else:
                    while stack:
                        y = stack.pop()
                        if cal_dict[y]:
                            ans.append(y)
                        else:
                            stack.append(y)
                            break
                stack.append(i)
    while stack:
        ans.append(stack.pop())
        print(f'#{tc} {"".join(ans)}')