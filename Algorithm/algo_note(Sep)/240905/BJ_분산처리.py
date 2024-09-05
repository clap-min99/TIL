# 1009 분산처리
T = int(input())

nums = [[i] for i in range(10)]  # 0부터 9까지 하나씩 들어있는 리스트 만들기

'''
거듭제곱의 1의 자리 수는 반복된다는 특징이 있다.
직접 거듭제곱을 해서 1의 자리를 찾으면 메모리가 터질 수 있으므로
반복되는 1의 자리 숫자들만 찾아서 리스트에 순서대로 넣었다.
'''

for i in range(10):
    x = 2
    while True:
        if int(str(i**x)[-1]) in nums[i]: 
            break
        last_num = str(i**x)[-1]
        nums[i].append(int(last_num))
        x += 1

for i in range(T):
    a, b = map(int, input().split())
    a_ = int(str(a)[-1])        # 1의 자리만 쓸 것이다.
    # 거듭제곱 해야할 값(b)을 리스트 안에 있는 개수만큼 나눠줬을 때의
    # 나머지를 찾으면 된다.
    if a_ == 0:
        print(nums[0][a_])
    else:    
        div_num = len(nums[a_])     # 1의 자리 숫자에 따라 나눠야할 리스트 길이가 다르다.
        rem = b % div_num    
        print(nums[a_][rem-1])
