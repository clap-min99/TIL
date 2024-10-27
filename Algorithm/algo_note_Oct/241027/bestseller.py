# 1302 베스트셀러
import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())

words = [input().strip() for _ in range(N)]
cnt_words = list(Counter(words).most_common())

max_num = cnt_words[0][1]

max_lst = []
for i in range(len(cnt_words)):
    if cnt_words[i][1] == max_num:
        max_lst.append(cnt_words[i])
max_lst.sort()
print(max_lst[0][0])