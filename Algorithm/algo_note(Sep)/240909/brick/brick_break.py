import sys
sys.stdin = open('input.txt')

dij = [[1,0],[-1,0],[0,1],[0,-1]]

def shoot(level, remains, now_arr):
    global min_blocks

    # 기저조건
    # 구슬을 모두 발사 or  남은 벽돌이 0이면 종료
    if level == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    # 한줄씩 쏘기
    for col in range(W):
        # 방법 1.
        # col 위치에 쏘기 전 상태 복사
        # 복사한 리스트의 col 위치에 구슬 쏘기
        # level + 1 번 상태로 이동(다음 재귀 호출)
        # col 위치에 쏘기 전 상태로 복구

        # 방법 2.
        # col 위치에 쏘기 전 상태 복사
        # 복사한 리스트의 col 위치에 구슬을 쏜다.
        # level + 1 번 상태로 이동 + col 위치에 쏘고 난 상태를 함께 전달
        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬 쏘기
        # 첫번째 만나는 벽돌 위치
        row = -1  # 벽돌이 없다고 가정
        for r in range(H):
            if copy_arr[r][col]:    # r위치에 벽돌이 있다면
                row = r     # 가장 위
                break
            if row == -1:       # 벽돌이 없는 열이면 다음 열로
                continue
            # 연쇄적으로 벽돌이 깨짐
            li = [(row, col, copy_arr[row][col])]  # 앞으로 깨져야할 벽돌들 저장
            now_remains = remains - 1       # 현재 남은 벽돌 -1
            copy_arr[row][col] = 0          # 구슬이 처음 만나는 벽돌 깨짐 처리

            while li:
                r, c, p = li.pop()
                for k in range(1, p):  # 파워만큼 퍼지면서 깨진다.
                    for di, dj in dij:
                        nr = r + k*di
                        nc = c + k*dj

                        if nr < 0 or nr >= H or nc < 0 or nc >=W:
                            continue

                        if copy_arr[nr][nc] == 0:
                            continue

                        li.append((nr, nc, copy_arr[nr][nc]))
                        copy_arr[nr][nc] = 0        # 벽돌 깨짐
                        now_remains -= 1
            # 빈칸 메꾸기
            for c in range(W):
                idx = H - 1
                for i in range(H-1, -1, -1):
                    if copy_arr[r][c]:
                        # idx 와 r이 같아도 바꿈(의미 없는 교환도 해쥼)
                        copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                        idx -= 1
            shoot(level+1, now_remains, copy_arr)


T = int(input())

for tc in range(1, T+1):

    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_blocks = 1e9
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el:  # 0보다 크면 벽돌
                blocks += 1

    shoot(0, blocks, arr)

    print(f'#{tc} {min_blocks}')