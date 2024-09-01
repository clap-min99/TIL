from collections import deque
T = 10

def make_pw(password):
    d = deque(password)    
    while True:
        for i in range(1, 6):
            d[0] = d[0] - i
            if d[0] <= 0:
                d[0] = 0
                d.rotate(-1)
                return d                
            d.rotate(-1)



for testcase in range(1, T +1):
    tc = int(input())
    pw = map(int, input().split())
    list_pw = list(make_pw(pw))
    
    print(f'#{tc}', *list_pw)




