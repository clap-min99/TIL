# 17219 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
address = {}
for _ in range(N):
    site, pw = input().split()
    address[site] = pw

find = []
for _ in range(M):
    a = input()[:-1]
    print(address[a])
