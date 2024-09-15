N, M = map(int, input().split())
article = list(map(int, input().split()))
people = N*M
for i in range(5):
    print(f'{article[i] - people}', end = " ")