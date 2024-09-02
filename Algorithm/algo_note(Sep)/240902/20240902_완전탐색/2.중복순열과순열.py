path = []
used = []
N = 0


def type1(x):
    if x == N:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        type1(x + 1)
        path.pop()


def type2(x):
    if x == N:
        print(path)
        return

    for i in range(1, 7):
        if used[i]:
            continue

        used[i] = True
        path.append(i)
        type2(x + 1)
        path.pop()
        used[i] = False


N, type = map(int, input().split())
used = [False for _ in range(7)]

if type == 1:
    type1(0)

if type == 2:
    type2(0)

