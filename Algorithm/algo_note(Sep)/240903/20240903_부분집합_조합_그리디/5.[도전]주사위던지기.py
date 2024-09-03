N = 3
path = []


def run(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev + 1, i)
        path.pop()


run(0, 1)
