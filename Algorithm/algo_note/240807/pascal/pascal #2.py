# pascal_recursive

def pascal_triangle(n):
    if n == 1:
        return [1]
    # 재귀적으로 파고들어서 첫 번째 행부터 값을 구해서 위로 올라감
    prev_row = pascal_triangle(n-1)

    # 새로운 행의 시작은 항상 1
    new_row = [1]

    # 이전 행의 2개의 값을 더해서 새로운 행에 추가
    # 여기서 이전 행은 재귀적으로 구해나간다
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])

    # 새로운 행의 마지막은 항상 1
    new_row.append(i)

    return new_row

T = int(input())