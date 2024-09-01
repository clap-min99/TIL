T = 10
for tc in range(1, T+1):
    
    def search(node):   # 해당 노드 정보를 토대로 왼쪽, 오른쪽 조사
        if node != 0:   # 그 노드 값이 0이 아니라면,
            # print(node)              # 전위 순회일 때
            search(tree[node][0])      # 왼쪽을 조사
            print(tree_info[node], end='')     # 중위 순회일 때
            search(tree[node][1])      # 오른쪽을 조사

    N = int(input())
    info = [list(input().split()) for _ in range(N)]  # 입력 받아서
    for x in range(N):          # 억지로 네칸씩 만들어줬습니다(../)
        if len(info[x]) == 4:
            continue
        elif len(info[x]) == 2:             
            info[x] = info[x] + [0,0]       
        elif len(info[x]) == 3:
            info[x] = info[x] +[0]
    
    tree_info = [0]
    for i in range(N):
        tree_info.append(info[i][1])    # 각 정점에 따라 알파벳을 리스트에 저장    
 
    tree = [[0,0] for _ in range(N+1)]
   
    for i in range(1, len(info)+1):        
        tree[i][0] = int(info[i-1][2])
        tree[i][1] = int(info[i-1][3])
        
    print(f'#{tc}', end=' ')
    search(1)
    print()
