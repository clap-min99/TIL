import sys
input = sys.stdin.readline



# 풀이 1 
# N = int(input())
# arr = list(int(input()) for _ in range(N))

# cnt = 0
# i = 0

# for i in range(N-1):
#     a = arr[i]
#     comp = arr[i+1:]
#     for j in range(len(comp)):
#         if a < comp[j]:
#             cnt += 1
#             break
#         if a >= comp[j]:
#             cnt += 1
#             continue
# print(cnt)

# 시간 초과,,, 

# 풀이 2
stack = []

