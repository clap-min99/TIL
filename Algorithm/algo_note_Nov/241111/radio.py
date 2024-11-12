# 3135 라디오
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input())
fqs = []
for _ in range(N):
    fq = int(input())
    fqs.append(fq)

sub = abs(A-B)

