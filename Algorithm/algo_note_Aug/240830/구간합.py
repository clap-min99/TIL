T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_lst = []
    for i in range(N-M+1):
        sum_lst.append(sum(arr[i:i+M]))
    sum_lst.sort()
    ans = sum_lst[-1] - sum_lst[0]
    print(f'#{tc} {ans}')
