# 2559 수열
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp_arr = list(map(int, input().split()))
pre = []
add_sum = 0
sum_list = []
for i in temp_arr:
    add_sum += i
    pre.append(add_sum)

for x in range(N-K+1):
    sum_list.append(pre[x+K]- pre[x])
print(max(sum_list))



# for i in range(N-K+1):
#     t_sum = 0
#     for j in range(K):
#         t_sum += temp_arr[j+i]
#     result.append(t_sum)
