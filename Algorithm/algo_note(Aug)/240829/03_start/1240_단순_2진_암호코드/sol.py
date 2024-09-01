import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    code = []
    idx = []
    for i in range(N):
        for j in range(M-1, 0, -1):     # 뒤에서부터 1이 처음 등장하는 인덱스 찾기
            if arr[i][j] == 1:
                x, y = i, j
                idx.append([x, y])
                break

    x, y = idx[0][0], idx[0][1]    # 인덱스를 x, y에 할당

    for a in range(56):
        code.append(arr[x][y-a])    # 1이 처음 등장하는 인덱스 앞의 56개가 암호
    code.reverse()                  # 거꾸로 넣었으니까 뒤집어주기
    pre_code = []
    code_lst = []
    for a in range(8):                          # 길이가 56인 코드를 7개씩 끊어넣으므로
        for b in range(7):                      # 7개씩 끊어서 넣기
            pre_code.append(str(code[7*a+b]))   # 문자열로 바꿔야 join으로 합칠 수 있다.
        code_lst.append(''.join(pre_code))      # 암호형태로 만들어서 코드리스트에 넣고
        pre_code = []                           # 초기화
    code_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    for i in range(8):
        code_lst[i] = code_dict[code_lst[i]]    # 암호를 숫자로 변환

    check = 0
    even = 0
    odd = 0
    for i in range(4):
        even += code_lst[2*i]
        odd += code_lst[2*i+1]

    if (3*even+odd)%10 == 0:
        ans = even + odd
    else:
        ans = 0
    print(f'#{tc} {ans}')

