from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append((i+1, cheeze[i]))

    pizzahut = []
    for c in range(N):
        pizzahut.append(pizza[c][1])

    print(pizzahut)

    # while True:
    #     for c in range(N):
    #         pizza[c][2] = pizza[c][2]//2

    #         if pizza[c][2] == 0:
                

    #             if not cheeze
    
        