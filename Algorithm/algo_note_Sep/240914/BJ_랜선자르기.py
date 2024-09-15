import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start = 1
end = max(lan)

while start <= end:
    mid = (start + end)//2
    lines = 0
    for i in lan:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else: 
        end = mid -1

print(end)
