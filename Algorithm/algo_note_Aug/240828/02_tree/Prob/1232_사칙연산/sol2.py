def cal(left, right, op):
    return eval(f'{left} {op} {right}')


def postorder(node):
    if type(arr[node][1]) == type(''):
        left = postorder(arr[node][2])
        right = postorder(arr[node][3])
        return cal(left, right, node)

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split()))]
