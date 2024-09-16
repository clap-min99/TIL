# 1620 나는야 포켓몬 마스터
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_to_name = {}
name_to_num = {}
for i in range(N):
    pokemon = input()[:-1]
    num_to_name[i+1] = pokemon
    name_to_num[pokemon] = i+1
print(num_to_name[25])
print(name_to_num['Raichu'])
for j in range(M):
    find = input()[:-1]
    if find.isdigit():
        print(num_to_name[int(find)])
    else:
        print(name_to_num[find])