arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3


def run(lev, start):        # lev번째는 start부터 뽑아라.
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1)
        path.pop()


run(0, 0)
