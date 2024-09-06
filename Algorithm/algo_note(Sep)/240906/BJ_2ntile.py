# 11726 2xn 타일링

n = int(input())
sum_lst = [1]

for i in range(n-1):
    a = sum_lst[i] + sum_lst[i-1]
    sum_lst.append(a)

print(sum_lst[-1] % 10007)