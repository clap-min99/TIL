# 2609 최대공약수와 최소공배수
N, M = map(int, input().split())
N_list = []
M_list = []
for i in range(1, N+1):
    if N % i == 0:
        N_list.append(i)
N_set = set(N_list)

for i in range(1, M+1):
    if M % i == 0:
        M_list.append(i)
M_set = set(M_list)

ans1 = max(N_set&M_set)
print(ans1)

a = []
b = []
for i in range(1, N+M):
    a.append(N*i)
    b.append(M*i)
a_set = set(a)
b_set = set(b)

ans2 = min(a_set&b_set)
print(ans2)