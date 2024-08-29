N = int(input())
sum_ = 0
line = sorted(map(int, input().split()))
for i in range(1, N+1):
    sum_ += sum(line[:i])
print(sum_)
