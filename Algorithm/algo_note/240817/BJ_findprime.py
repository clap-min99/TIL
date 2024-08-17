#1978 소수찾기

def is_prime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1

cnt = 0
N = int(input())
nums = list(map(int, input().split()))
for i in range(N):
    cnt += is_prime(nums[i])

print(cnt)
