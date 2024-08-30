
def search(node):
    if node != 0:
        search(tree[node][0])
        in_order.append(node)
        search(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0, 0] for _ in range(N+1)]

    for i in range(1, N//2+1):
        tree[i][0] = 2*i
        if 2*i+1 <= N:
            tree[i][1] = 2 * i + 1

    in_order = [0]
    search(1)

    root = in_order.index(1)
    ans = in_order.index(N//2)
    print(f'#{tc} {root} {ans}')