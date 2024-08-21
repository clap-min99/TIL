N = int(input())
shirt = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0
for i in range(len(shirt)):
    if shirt[i] % T == 0:
        cnt += shirt[i]//T
    elif shirt[i] % T != 0:
        cnt += shirt[i]//T +1

pen_bundle = N//P
pen = N%P 

print(cnt)
print(f'{pen_bundle} {pen}')
