T = int(input())

for tc in range(1, T+1):
    op_dict = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}  # 숫자가 높을수록 우선순위 높다
    stack = []      # 연산자를 저장할 스택
    postfix = []    # 후위 표기식을 저장할 리스트
    forth_code = list(input())

    for ex in forth_code:
        if ex.isnumeric():
            postfix.append(ex)
        elif ex == '(':         # 여는 괄호는 스택에 추가
            stack.append(ex)
        elif ex == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()


