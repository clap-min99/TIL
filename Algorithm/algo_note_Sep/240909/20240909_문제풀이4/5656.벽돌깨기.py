import sys
sys.stdin = open('input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def shoot(level, remains, now_arr):
    global min_blocks

    # 기저조건
    # 구슬을 모두 발사 or 남은 벽돌이 0 이면 종료
    if level == N or remains == 0:
        min_blocks = min(min_blocks, remains)  # 최소값 갱신
        return

    # 한 줄씩 쏘자
    for col in range(W):
        # 방법1.
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 원본 리스트의 col 위치에 구슬을 쏜다
        # 3. level + 1 번 상태로 이동(다음 재귀 호출)
        # 4. col 위치에 쏘기 전 상태로 복구

        # 방법2. (복구 하는 시간이 너무 오래걸린다)
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 구슬을 쏜다.
        # 3. level + 1 번 상태로 이동(다음 재귀 호출) + col 위치에 쏘고 난 상태를 함께 전달
        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬을 쏘자!
        # 1. 구슬을 쏘는 열에서 가장 위에 있는 벽돌 찾기
        row = -1  # 벽돌이 없다고 가정
        for r in range(H):
            if copy_arr[r][col]:  # r 위치에 벽돌이 있다면
                row = r  # 가장 위
                break

        if row == -1:  # 벽돌이 없는 열이면 다음 열로 넘어가자
            continue

        # 2. 연쇄적으로 벽돌이 깨짐
        # 행, 열, 숫자(파워)
        li = [(row, col, copy_arr[row][col])]  # 앞으로 깨져야할 벽돌들을 저장
        now_remains = remains - 1   # 현재 남은벽돌 - 1
        copy_arr[row][col] = 0      # 구슬이 처음 만나는 벽돌 깨짐 처리

        while li:
            r, c, p = li.pop()
            for k in range(1, p):   # 파워만큼 퍼지면서 깨진다.
                for i in range(4):  # 상하좌우
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:  # 범위 계산
                        continue

                    if copy_arr[nr][nc] == 0:  # 벽돌이 없다면 통과
                        continue

                    li.append((nr, nc, copy_arr[nr][nc]))  # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0                   # 벽돌 깨짐
                    now_remains -= 1                       # 숫자 감소

        # 빈칸 메꾸기
        for c in range(W):  # 전체 열들을 확인
            idx = H - 1  # 벽돌이 위치할 index
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:  # 벽돌이 있으면 무조건 swap 하도록
                    # idx 와 r 이 같아도 바꾼다 == 의미없는 교환
                    # 가독성을 위해서 아래와 같이 구현
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(level + 1, now_remains, copy_arr)


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    
    # 1. 최소 벽돌
    #  - 몇 개 남았을까? 계산해야 한다. -> 2차원 리스트를 순회하면서 매 번 계산하면 너무 느리다!
    #  - 현재 남은 벽돌 수를 통해 해결됨!
    # 2. 현재 벽돌이 다 깨지면(남은 벽돌이 없다) 더 이상 진행할 필요가 없다!
    #  - 현재 남은 벽돌 수 같이 저장하면 좋을 것 같다.
    # 3. N 번 구슬을 쏘자.
    #  - 시작점: 0번 / 하나도 안깨진 벽돌 수
    #  - 끝점: N번 쏘면 끝 / 벽돌이 다 깨지면 끝

    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el:  # 0보다 크면 벽돌임
                blocks += 1

    shoot(0, blocks, arr)

    print(f'#{tc} {min_blocks}')
    
    
    