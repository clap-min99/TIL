# 3015 오아시스 재결합

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
N = int(input())
oasis = list(int(input()) for _ in range(N))

stack = []      # (키, cnt)
result = 0

for i in oasis:
    while stack and stack[-1][0] < i:
        result += stack.pop()[1]

    if not stack:
        stack.append((i, 1))
        continue

    # 스택 끝 값의 키와 같을 때
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        result += cnt

        if stack:
            result += 1
        stack.append((i, cnt+1))

    # 스택 끝 값의 키보다 작으면
    else:
        stack.append((i, 1))
        result += 1

print(result)
