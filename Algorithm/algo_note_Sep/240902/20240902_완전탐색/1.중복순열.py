path = []


def kfc(x):
    if x == 3:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        kfc(x + 1)
        path.pop()


kfc(0)
