'''
input

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

T = int(input())
li = []
for _ in range(T):
    li.append(list(map(int, input().split())))

# 1. 끝나는 시간 / 2. 빨리 시작하는 시간 순서대로 정렬되어야 한다.
li.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = -1
for meeting in li:
    # 끝나는 시간보다 크거나 같다 == 회의가 시작할 수 있다.
    # 즉, 회의가 시작할 수 있다면
    # 1. 정답에 1 추가
    # 2. 끝나는 시간 초기화
    if meeting[0] >= end:
        cnt += 1
        end = meeting[1]

print(cnt)
