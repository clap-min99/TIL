T = int(input())

for tc in range(1, T+1):
    N = int(input())
    path = list(map(int, input().split()))  # 등산경로 입력받기
    x = []       # 오르막을 구분할 수 있는 리스트
    for h in range(N-1):
        if path[h] > path[h+1]:
            x.append(h)

    x.append(N-1)  # 편의상 마지막 길이 더해준 리스트 생성
    x.insert(0, 0)

    easy_path = []
    for i in range(len(x)-1):
        if i == 0:
            A = path[x[i+1]]    # 가장 높은 값
            B = path[x[i]]      # 가장 낮은 값
            C = x[i+1] - x[i] + 1
            ang_0 = (A-B)/C
            easy_path.append(ang_0)
        else:
            if i > 0:
                A = path[x[i+1]]
                B = path[x[i]+1]
                C = x[i+1] - x[i]
                ang_1 = (A-B)/C
                easy_path.append(ang_1)
    print(easy_path)