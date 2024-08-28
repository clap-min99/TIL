import sys
sys.stdin = open('input.txt')


def cal(left, right, oper):
    return eval(f'{left} {oper} {right}')
    # if oper == '+':
    #     return left + right
    # elif oper == '-':
    #     return left - right
    # elif oper == '*':
    #     return left * right
    # elif oper == '/':
    #     return left / right

def postorder(node):
    '''
        이번에는 트리를 구성할 때 없는 자식 노드 번호는 기록하지 않았다.
        왼쪽, 오른쪽 자식이 반드시 있는 경우가 있다.
        WHEN? -> '연산자'인 경우!
        arr[node][1] '+-*/'
    '''
    # 'in'은 시퀀스 연산자. 즉, 순서가 있는 자료형
    # if arr[node][1] in '+-*/'
    # if arr[node][1] in ['+','-','*','/']
    if type(arr[node][1]) == type(''):
        left = postorder(arr[node][2])
        right = postorder(arr[node][3])
        return cal(left, right, arr[node][1])
    else:
        return arr[node][1]     # 이게 연산자


for tc in range(1, 11):
    N = int(input())
    # node 번호 인덱스로 사용할 값만 int로 형변환해서 tree 정보 기록
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    arr.insert(0,0)
    result = postorder(1)
    print(f'#{tc} {int(result)}')
