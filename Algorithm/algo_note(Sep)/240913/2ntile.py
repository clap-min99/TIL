# 11727 2*n 타일링 2

n = int(input())

ans = [0, 1, 3]
if n >=3 :
    for i in range(3, n+1):
        a = 2*ans[i-2] + ans[i-1]
        ans.append(a)
print(ans[n])