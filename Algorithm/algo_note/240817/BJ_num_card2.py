import sys
input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))
ans = []
for i in find_num:
    a = card_list.count(i)
    ans.append(a)
print(*ans)