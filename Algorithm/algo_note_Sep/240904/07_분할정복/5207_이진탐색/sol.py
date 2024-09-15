# import sys
# sys.stdin = open('input.txt')


def bin_search(low, high, arr, target):    # 시작점, 끝점, 기본 배열, 타겟값
    check = 0
    while low <= high:
        mid = (low+high)//2

        if arr[mid] < target:     # 타겟이 오른쪽
            if check == 1:         # 다시 오른쪽으로 왔으면 넘기기
                return False
            low = mid + 1           # 타겟이 오른쪽에 있으면 최솟값을 mid+1로
            check = 1               # 오른쪽 검사 표시

        elif arr[mid] > target:       # 타겟이 왼쪽에
            if check == -1:             # 다시 왼쪽으로 왔으면 넘기기
                return False
            high = mid -1
            check = -1              # 왼쪽 검사 표시

        else:                   # 중앙값이랑 타겟이랑 같으면
            return True         # True

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

