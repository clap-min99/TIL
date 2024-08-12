T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    prev = [1]
    print(1)

    for i in range(1, N):
        cur = [1]
        for j in range(len(prev)-1):
            cur.append(cur[j]+cur[j+1])
        cur.append(1)

        print(' '.join(map(str, cur)))

        prev = cur
