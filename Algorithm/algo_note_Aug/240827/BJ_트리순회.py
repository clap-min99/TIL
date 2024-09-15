preorder= []
inorder = []
postorder = []

def search(node):
    if node != 0:
        preorder.append(node)
        search(tree[node][0])
        inorder.append(node)
        search(tree[node][1])
        postorder.append(node)

N = int(input())
arr = [list(input().split()) for _ in range(N)]

alp_to_num = {} # 알파벳을 숫자로 변환하는 dic
num_to_alp = {} # 숫자를 알파벳으로 변환
for i in range(1, N+1):
    alp_to_num[arr[i-1][0]] = i  # dictionary에 각 알파벳을 숫자로 저장
    num_to_alp[i] = arr[i-1][0]
alp_to_num['.'] = 0     # '.'은 0 으로 



tree = [[0, 0] for _ in range(N+1)]
for i in range(1, N+1):  # tree 만들기
    tree[i][0] = alp_to_num[arr[i-1][1]]
    tree[i][1] = alp_to_num[arr[i-1][2]]

search(1)
for i in range(N):
    preorder[i] = num_to_alp[preorder[i]]
    inorder[i] = num_to_alp[inorder[i]]
    postorder[i] = num_to_alp[postorder[i]]

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))