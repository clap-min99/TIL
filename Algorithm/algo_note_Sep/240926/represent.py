import sys
input = sys.stdin.readline

arr = sorted(int(input()) for _ in range(5))
av = int(sum(arr) / 5)
mid = arr[2]
print(av)
print(mid)