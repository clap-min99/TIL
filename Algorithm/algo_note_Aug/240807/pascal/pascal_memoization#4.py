""""
memoization을 활용해서 구현
시간 복잡도: O(N^2)
개선된 재귀와 동일하게 코드를 작성하나
기존 행을 계산한 적 있으면 해당 값을 사용하며, 사용한 적이 없으면 계산한 다음 memo에 저장
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    # 파스칼 삼각형을 저장할 2차원 배열을 생성
    triangle = [[0] * N for _ in range(N)]

    for i in range(N):
        triangle[i][0] = 1
        triangle[i][i] = 1

    for i in range(N):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    for i in range(N):
