# 15663 N과 M(9)
import sys
input= sys.stdin.readline
from collections import deque

N, M  = map(int, input().split())
arr = set(map(int, input().split()))
ans_list = []
def nums():
    stack = []
    stack.append(arr[0])
    
    if len(stack) == M:
        ans_list.append()

