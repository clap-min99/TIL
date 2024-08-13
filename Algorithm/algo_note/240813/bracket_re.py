T = int(input())

def find_pair(codes):
    
    stack = []

    for i in codes:
        if i == '(':       # 열린 괄호를 만나면
            stack.append(i)
        if i == ')':
            if not stack or stack[-1] != '(':
                return 0
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        return 1
    
    return 0



for tc in range(1, T+1):
    brackets = input()    
    a = find_pair(brackets)
    print(f'#{tc} {a}')




            
                   
                
            