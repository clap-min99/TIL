import sys
input = sys.stdin.readline

T = int(input())

arr = []
for i in range(1,T+1):
    arr.append(int(input()))

arr.sort()

for j in range(len(arr)):
    print(arr[j])

# 2차원배열