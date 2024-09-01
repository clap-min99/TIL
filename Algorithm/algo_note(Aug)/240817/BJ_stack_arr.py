import sys
input = sys.stdin.readlines

n = int(input())
obj = []    # 내가 목표하는 순서 리스트
stack = []  
seq = []    # 1부터 n까지 숫자 리스트 


for i in range(1, n+1):
    seq.append(i)

for _ in range(n):
    a = int(input())
    obj.append(a)

while True:
    while seq[0] == obj[0]:
        stack.append(seq.pop(0))


