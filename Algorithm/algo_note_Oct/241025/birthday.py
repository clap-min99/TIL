# 5635 생일
import sys
input = sys.stdin.readline

n = int(input())
info = []

for _ in range(n):
    name, day, mon, year = input().split()
    info.append([name, int(day), int(mon), int(year)])

arr_info = sorted(info, key=lambda x: (x[3], x[2], x[1]))

print(arr_info[-1][0])
print(arr_info[0][0])
