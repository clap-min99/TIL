# 15829 Hashing
L = int(input())
convert = list(input())
alp = 'abcdefghijklmnopqrstuvwxyz'
alp_to_num = {}
mod = 1234567891
for i in range(26):
    alp_to_num[alp[i]] = i+1

ans = 0
for i in range(L):
    a = alp_to_num[convert[i]] * (31**i)
    ans += a
print(ans%mod)