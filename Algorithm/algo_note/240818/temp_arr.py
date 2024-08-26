# 2559 수열
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp_arr = list(map(int, input().split()))
pre = [0]
add_sum = 0
sum_list = []
for i in temp_arr:
    add_sum += i
    pre.append(add_sum)

for x in range(N-K+1):
    sum_list.append(pre[x+K]- pre[x])
print(max(sum_list))

# 구간합을 구하는 시간 복잡도가 O(n), m번 동안 수행하면 총 시간복잡도는 O(nm)
# 매번 구간합을 구하는게 아니라 길이 n짜리 리스트를 만들어 그 자리 까지의 누적합을 저장
# 각 자리의 누적합에서 빼주는 방식으로 구간합 구하기. 

# for i in range(N-K+1):
#     t_sum = 0
#     for j in range(K):
#         t_sum += temp_arr[j+i]
#     result.append(t_sum)
