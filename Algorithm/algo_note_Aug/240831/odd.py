all_lst = [int(input()) for _ in range(7)]
odd_lst = []
for i in range(7):
    if all_lst[i]%2 == 1:
        odd_lst.append(all_lst[i])

odd_lst.sort()

if odd_lst:
    print(sum(odd_lst))
    print(odd_lst[0])
else:
    print(-1)

