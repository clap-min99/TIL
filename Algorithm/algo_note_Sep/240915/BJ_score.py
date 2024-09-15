# 2822 점수계산
import sys
input = sys.stdin.readline
score_lst = []
for i in range(8):
    score = int(input())
    score_lst.append((score,i+1))
sort_score = sorted(score_lst, key = lambda x: -x[0])[:5]
sum_ = 0
prob_num = []
for i in range(5):
    sum_ += sort_score[i][0]
    prob_num.append(sort_score[i][1])
prob_num.sort()
print(sum_)
print(*prob_num)