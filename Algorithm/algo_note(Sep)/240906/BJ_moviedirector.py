# 1436 영화감독 숌

N = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1
    if cnt == N:
        break
    result += 1
    # 찾을 때 까지 1씩 더하면서 666이 문자열에 포함되면 +1

print(result)