
for i in range(10):    #10개의 테스트 케이스
    N = int(input())   # 건물 개수 N
    for j in range(N):
        H = list(map(int, input().split())) #건물 높이 H
        add_view = 0
        view_list = []
        for k in range(i-2, i+3):
            view_list.append(H[i]-H[k])
            if H[i] == H[k]:
                view_list.remove(H[i]-H[k])
            elif H[i] < H[k]:
                view_list.remove(H[i]-H[k])
            else:
                if H[i] > H[k]:
                    continue
        add_view += min(view_list)
        print(view_list)
        # print(f'#{i} {add_view}')


