# 2535 아시아 정보올림피아드
import sys
input = sys.stdin.readline

N = int(input())

contest = []
cnt = 1
for i in range(N):
    nat, stud, score = map(int, input().split())
    contest.append((nat,stud,score))


contest_sort = sorted(contest, key=lambda x: -x[2])

for i in range(2):
    print(contest_sort[i][0], contest_sort[i][1])

if contest_sort[0][0] == contest_sort[1][0]:
    for i in range(2, N):
        if contest_sort[1][0] != contest_sort[i][0]:
            print(contest_sort[i][0], contest_sort[i][1])
            break
else:
    print(contest_sort[2][0], contest_sort[2][1])
    
