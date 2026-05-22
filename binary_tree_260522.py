# 1. 딕셔너리 이용
tree = {}
tree['A'] = ['B', 'C']
tree['B'] = ['D', 'E']
tree['C'] = ['F', None]
tree['D'] = [None, None]
tree['E'] = [None, None]
tree['F'] = [None, None]

# 2. 전위 순회 
def preorder(node):
    if node is not None:
        print(node, end='')       
        preorder(tree[node][0])   
        preorder(tree[node][1])   

# 3. 중위 순회
def inorder(node):
    if node is not None:
        inorder(tree[node][0])   
        print(node, end='')      
        inorder(tree[node][1])    

# 4. 후위 순회
def postorder(node):
    if node is not None:
        postorder(tree[node][0])  
        postorder(tree[node][1])  
        print(node, end='')       

# 5. 입출력

print("전위 순회:", end = "")
preorder('A')
print()

print("중위 순회:", end = "")
inorder('A')
print()

print("후위 순회:", end = "")
preorder('A')
print()

