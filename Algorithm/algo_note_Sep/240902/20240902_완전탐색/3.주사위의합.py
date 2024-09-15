path = []


def kfc(x, sum):
    if sum > 10:
        return

    if x == 3:
        if sum <= 10:
            print(f'{path} = {sum}')

        return

    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()


kfc(0, 0)
