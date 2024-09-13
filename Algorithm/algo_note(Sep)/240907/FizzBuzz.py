# 28702 FizzBuzz

FB = [input() for i in range(3)]
for i in range(2,-1,-1):
    if FB[i].isdigit():
        ans = int(FB[i]) + (3-i)

if ans % 15 == 0:
    print('FizzBuzz')
elif ans % 5 == 0:
    print('Buzz')
elif ans % 3 == 0:
    print('Fizz')
else:
    print(ans)