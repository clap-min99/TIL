# Sol_by_T -> 내가 스스로 짜보기

# row, col이 주어졌을 때, 이전 row와 col을 구해가면서 현재 row, col을 구하는 재귀함수
def pascal_triangle(row, col):
    if col == 0 or col == row:      # 첫 번째 값, 마지막 값일 때 1 반환
        return 1
    # 재귀적으로 두 값을 더함
    return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)
    # 현재 값에서 바로 위의 왼쪽 값 + 바로 위의 값


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    for i in range(N):
        row = []
        for j in range(i + 1):
            row.append(str(pascal_triangle(1, j)))
        print(' '.join(row))
