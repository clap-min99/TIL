arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']


# path 출력 함수
def print_name():
    print(path, end=' / ')
    print('{ ', end='')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')


def run(lev):
    # 3개를 뽑았을 때 출력
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()


run(0)
