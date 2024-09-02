'''
2 3 5 7 7 7
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

arr = []
used = [False for _ in range(6)]
path = []
is_found_baby_gin = False


def is_baby_gin():
    cnt = 0

    # 앞에 세 자리가 triplet 또는 run 이라면 cnt += 1을 수행
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == (b - 1) == (c - 2):
        cnt += 1

    # 뒤에 세 자리가 triplet 또는 run 이라면 cnt += 1을 수행
    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == (b - 1) == (c - 2):
        cnt += 1

    # cnt 가 2 라면, baby-gin 이 맞다.
    return cnt == 2


def run(lev):
    global is_found_baby_gin
    if lev == 6:
        # baby-gin인지 검사하는 코드
        if is_baby_gin():
            is_found_baby_gin = True

        return

    for i in range(6):
        if used[i]:
            continue
        used[i] = True
        path.append(arr[i])
        run(lev + 1)
        path.pop()
        used[i] = False


arr = list(map(int, input().split()))
#arr = [2, 3, 5, 7, 7, 7]

run(0)

if is_found_baby_gin:
    print('Yes')
else:
    print('No')