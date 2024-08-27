T = int(input())
# 구해야 하는 것
# 루트에 저장된 값
# N/2에 저장된 값
for tc in range(1, T+1):
    N = int(input())
    
    tree = [[0,0] for _ in range(N+1)]

    for i in range(1, (N)//2+1):
        tree[i][0] = 2*i            
        if 2*i+1 <= N:
            tree[i][1] = 2*i + 1
    print(tree)


    in_order = [0]      # 중위 순회
    def search(node):
        if node != 0:
            search(tree[node][0])
            in_order.append(node)
            search(tree[node][1])

    search(1)


    root = in_order.index(1)
    find_node = in_order.index(N//2)

    print(f'#{tc} {root} {find_node}')
