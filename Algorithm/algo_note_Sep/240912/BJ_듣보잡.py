# 1764 듣보잡
N, M = map(int, input().split())

N_set = set()
M_set = set()
for _ in range(N):
    not_heard = input()
    N_set.add(not_heard)
for _ in range(M):
    not_seen = input()
    M_set.add(not_seen)
ans_lst = sorted(N_set&M_set)

length = len(ans_lst)
print(length)
for name in ans_lst:
    print(name)