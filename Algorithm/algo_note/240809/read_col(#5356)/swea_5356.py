T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    col = []
    for i in range(15):
        for j in range(len(arr)):
            if i >= len(arr[j]):
                continue
            col.append(arr[j][i])

    print(f'#{tc}', ''.join(col))
