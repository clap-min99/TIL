card = ['A', 'J', 'Q', 'K']
path = []
cnt = 0


def cont_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False


def permu(lev):
    global cnt
    if lev == 5:
        if cont_three():
            cnt += 1
        return

    for i in range(4):
        path.append(card[i])
        permu(lev + 1)
        path.pop()


permu(0)
print(cnt)
