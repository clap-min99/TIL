# 1003 수 정렬하기 3
# 메모리 초과... 
# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = []
# for i in range(N):
#     a = int(input())
#     arr.append(a)
# arr.sort()
# for i in range(N):
#     print(arr[i])

import sys
input = sys.stdin.readline

n = int(input())


count = [0]*10001

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)