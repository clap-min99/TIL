# 1918 후위표기식
import sys
input = sys.stdin.readline

"""
1. 피연산자가 자오는 경우 결과에 추가
2. 여는 괄호가 나오면 스택에 추가
3. 닫힌 괄호가 나올 경우, 열린 괄호를 만날 때까지 연산자를 꺼내서 결과에 추가
4. 연산자가 나오는 경우, 스택 가장 위에 연산자가 현재 비교하려는 연산자보다 우선순위가 높거나 같다면 스택에서 제거 후 결과에 추가
   우선순위가 낮은 연산자를 만날 때까지 4번 과정 반복 후, 현재 비교하려는 연산자를 스택에 추가
5. 모든 문자에 대해서 1~4과정을 진행한 후에 스택에 남아있는 모든 연산자를 후위표기식에 추가
"""

def infix_to_postfix(expression):
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(':0 , ')': 0}
    stack = []
    postfix = []
    for ex in expression:
        if ex.isalpha():
            postfix.append(ex)
        elif ex == '(':
            stack.append(ex)
        elif ex == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()
        # 연산자일때
        else:
            while stack and op_dict[stack[-1]] >= op_dict[ex]:
                postfix.append(stack.pop())
            stack.append(ex)
        
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

infix = input()[:-1]
ans = infix_to_postfix(infix)
print(ans)