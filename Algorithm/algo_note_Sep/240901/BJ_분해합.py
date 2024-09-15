# 2231 분해합
N = int(input())

for i in range(N):
    result = sum(int(x) for x in str(i))    
    # N보다 작은 숫자를 문자열로 해서 각 숫자를 하나씩 더하기
    result += i
    # 각 자리 합과 그 숫자를 더한 값을 result에 할당
    if result == N: # 그 값이 원하는 값과 같으면 출력
        print(i)
        break
else:
    print(0)