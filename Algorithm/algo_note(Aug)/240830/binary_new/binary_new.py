def search(node):
    if node != 0:
        search(tree[node][0])
        tree_codes.append(node)
        search(tree[node][1])

T = int(input())

for tc in range(1, T+1):
    code = list(input())
    N = int(code.pop(0))        # salt 계산용 숫자 따로 뺴내기

    code_lst = []
    for i in range(8):
        a, b = code[2*i], code[2*i+1]
        code_lst.append(''.join([a, b]))    # 암호열 두자리씩

    for i in range(8):
        code_lst[i] = int(code_lst[i], 16)  # 16진수 문자열 10진수로 변환

    salt = [N*i for i in range(1, 9)]

    real_code = []
    for i in range(8):
        real_code.append(code_lst[i]-salt[i])

    tree = [[0,0] for _ in range(10)]
    for i in range(1, 5):
        tree[i][0] = 2*i
        if 2*i +1 <= 8:
            tree[i][1] = 2*i +1

    tree_codes = []
    search(1)

    arr_code = []
    for i in range(1, 9):
        arr_code.append(real_code[tree_codes.index(i)])
    
    print(f'#{tc}', end =' ')
    for i in range(8):
        a = str(arr_code[i])
        print(a[-1] , end ='')
    print()

