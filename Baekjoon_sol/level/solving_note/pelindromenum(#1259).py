while True:
    a = input()
    b = a[::-1]
    if a == '0':
        break
    elif a == b:
        print('yes')
    else:
        if a != b:
            print('no')
