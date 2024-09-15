import sys
sys.stdin = open('input.txt')


def merge_sort(div_arr):
    global result

    if len(div_arr) <= 1:
        return div_arr

    mid = len(div_arr) //2      # 파티션 나눌 기준점
    left = merge_sort(div_arr[:mid])    # 기준점 왼쪽 전부
    right = merge_sort(div_arr[mid:])   # 기준점 포함 오른쪾 전부

    left_idx, right_idx, k = 0, 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            div_arr[k] = left[left_idx]
            left_idx += 1
        else:
            div_arr[k] = right[right_idx]
            right_idx += 1
        k+=1

    if left_idx < len(left):
        div_arr[k:] = left[left_idx:]
    if right_idx < len(right):
        div_arr[k:] = right[right_idx:]

    if left[-1] > right[-1]:
        result += 1
    return div_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    result = 0
    arr = merge_sort(data)
    print(f'#{tc} {arr[N//2]} {result}')