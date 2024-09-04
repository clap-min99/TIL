import sys
sys.stdin = open('input.txt')


def bin_search(start, end, arr, target):
    check = 0
    while start <= end:
        mid = (start+end)//2

        if arr[mid] < target:     # 타겟이 오른쪽
            if check == 1:
                return False
            start = mid + 1
            check = 1

        elif arr[mid] > target:       # 타겟이 왼쪽에
            if check == -1:
                return False
            end = mid -1
            check = -1

        else:   # 중앙값이랑 타겟이랑 같으면
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    ans = 0
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(len(B)):
        if bin_search(0, N-1, A, B[i]):
            ans += 1
    print(f'#{tc} {ans}')

