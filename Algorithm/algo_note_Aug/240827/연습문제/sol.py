# import sys
# sys.stdin = open('input.txt')

def search(node):   # 해당 노드 정보를 토대로 왼쪽, 오른쪽 조사
    if node != 0:   # 그 노드 값이 0이 아니라면,
        print(node)                 # 전위 순회
        search(tree[node][0])      # 왼쪽을 조사
        # print(node)                 # 중위 순회
        search(tree[node][1])      # 오른쪽을 조사


V = int(input())        # 전체 노드 수
arr = list(map(int, input().split()))

# tree 정보를 입력할 수 있도록 하자.
# tree 리스트의 인덱스 번호 -> 부모 노드의 번호
# tree[parent] 위치의 리스트의 0번째 : 왼쪽 자식
# tree[parent] 위치의 리스트의 1번째 : 오른쪽 자식
tree = [[0,0] for _ in range(V+1)] # 0번 노드는 안쓰니까
for i in range(len(arr)//2):  # 간선 정보
    parent = arr[2*i]
    child = arr[2*i+1]
    if tree[parent][0] == 0:    # 아직 왼쪽 자식 정보 기록한적 없다면
        tree[parent][0] =  child
    else:                       # 왼쪽 자식에 정보 넣었는데 또 자식이 있으면
        tree[parent][1] = child  # 오른쪽 자식도 필요하다

search(1)