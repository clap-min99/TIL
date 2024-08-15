#11650 좌표 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
coordinate = []

for _ in range(N):
    a, b = map(int, input().split())
    coordinate.append([a,b])

coordinate.sort()

for a in range(N):
    print(*coordinate[a])


# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if coordinate[j][0] > coordinate[j+1][0]:
#             coordinate[j],coordinate[j+1] = coordinate[j+1],coordinate[j]
#         else:
#             if coordinate[j][0] == coordinate[j+1][0]:
#                 if coordinate[j][1] > coordinate[j+1][1]:
#                     coordinate[j],coordinate[j+1] = coordinate[j+1],coordinate[j]

# for a in range(N):
#      print(*coordinate[a])   
# 이렇게 하면 시간초과 남....