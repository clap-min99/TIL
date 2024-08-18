#2635 수 이어가기
N = int(input())
find_max = []
cnt_list = []
for i in range(N-1, 0, -1):
    cnt = 2
    sub_list= [N]
    sub_list.append(i)
    while True:
        j = sub_list[-2] - sub_list[-1]     # 가장 끝 두 수를 뺀 값이 j
        sub_list.append(j)
        cnt += 1
        if j < 0:
            sub_list.pop()
            cnt -= 1
            cnt_list.append(cnt)
            find_max.append([cnt, sub_list])
            break

print(max(cnt_list))
for i in range(N):
    if find_max[-i][0] == max(cnt_list):
        print(find_max[-i][0])
        print(*find_max[-i][1])





