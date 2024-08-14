sw_num = int(input())                       # 스위치 개수
sw_con = list(map(int, input().split()))    # 스위치 상태
# 스위치 번호는 1부터 시작함.
stu_num = int(input())                      # 학생 수

list_stu = []                               # 성별, 기준 수 저장할 리스트

ch_dict = {1: 0, 0: 1}

for _ in range(stu_num):
    sx, given_num = map(int, input().split())
    list_stu.append([sx, given_num])        # 성별, 받은 수?를 리스트에 저장

for i in range(stu_num):
    if list_stu[i][0] == 1:         # 남자이면
        ch_idx = []                 # 바꿔야 하는 인덱스를 받는 리스트
        for a in range(1, sw_num+1):    # a는 1번부터 스위치 번호까지
            if a % list_stu[i][1] == 0:     # 받은 수의 배수를 찾기 위해
                ch_idx.append(a)
        for b in range(len(ch_idx)):    # 받은 수 배수의 인덱스 값 바꾸기
            sw_con[ch_idx[b]-1] = ch_dict[sw_con[ch_idx[b]-1]]

    if list_stu[i][0] == 2:                     # 여자이면
        d = list_stu[i][1]                      # 주어진 수
        sw_con[d-1] = ch_dict[sw_con[d-1]]
        for x in range(d):           # 하나씩 더해가면서 검사(?)
            forward = d - 1 + x
            backward = d - 1 - x
            if 0<= forward < sw_num and 0<= backward <sw_num:
                if sw_con[forward] == sw_con[backward]:
                    sw_con[forward] = ch_dict[sw_con[forward]]
                    sw_con[backward] = ch_dict[sw_con[backward]]
                else:
                    break

for i in range(1, sw_num + 1):
    print(sw_con[i-1], end=' ')
    if i % 20 == 0:
        print()
