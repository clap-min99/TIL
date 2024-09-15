numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
cnt = 0  # 총 몇가지인지 계산
path = []


def recur(now, total):
    global cnt
    if now == 10:
        return

    if total + numbers[now] == 0:
        print(path + [numbers[now]])
        cnt += 1

    # 현재 수를 사용하지 않는 경우
    recur(now + 1, total)

    # 현재 수를 사용하는 경우: 경로에 추가, 누적합에 계산
    path.append(numbers[now])
    recur(now + 1, total + numbers[now])
    path.pop()


recur(0, 0)
print(f'총 {cnt}가지')
