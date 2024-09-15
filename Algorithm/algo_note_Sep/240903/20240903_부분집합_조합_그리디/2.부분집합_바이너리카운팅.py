arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1


for tar in range(0, 1 << n):  # range(0, 8)
    print('{', end='')
    get_sub(tar)
    print('}')
