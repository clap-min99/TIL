#2635 수 이어가기
N = int(input())
find_max = []
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
            find_max.append([cnt, sub_list])
            break

find_max.sort()
print(find_max[-1][0])
print(*find_max[-1][1])





