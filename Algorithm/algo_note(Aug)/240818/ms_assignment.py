# 민석이의 과제 체크하기

T = int(input())
for tc in range(1, T+1):
    N ,K = map(int, input().split())
    submit = set(map(int, input().split()))
    stu = []
    for i in range(1, N+1):
        stu.append(i)
    stu_set = set(stu)
    ans = list(stu_set - submit)
    print(f'#{tc}', *ans)