all_lst = [int(input()) for _ in range(7)]
odd_lst = []
for i in range(7):
    if all_lst[i]%2 == 1:
        odd_lst.append(all_lst[i])
odd_lst.sort()
ans1 = sum(odd_lst)
ans2 = odd_lst[0]
print(ans1)
print(ans2)