# 숫자카드 10816
from collections import Counter
import sys
input = sys.stdin.readline



n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

count = Counter(card_list)

for i in range(m):
    if find_num[i] in count:
        print(count[find_num[i]], end = ' ')
    else:
        print(0, end=' ')