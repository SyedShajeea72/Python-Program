class Node:
    def __init__(self,data):
        self.key=key
        self.left=None
        self.right=None
def insert(root,key):
        if root is None:
            return Node(key)
        if key < root.key:
               root.left=insert(root.left,key)
        elif key > root.key:
              root.right=insert(root.right,key)
        return root
def inorder(root):
        if  root:
           inorder(root.left)   
           print(root.key, end=' ') 
           inorder(root.right)
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        min_larger_node = min_value_node(root.right)
        root.key = min_larger_node.key
        root.right = delete(root.right, min_larger_node.key)
    return root
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = None
for key in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, key)
inorder(root)
key_to_search = 40
found = search(root, key_to_search)
print(f"\nSearch for {key_to_search}: {'Found' if found else 'Not Found'}")

# Delete a key
key_to_delete = 70
root = delete(root, key_to_delete)
print(f"\nInorder after deleting {key_to_delete}:")
inorder(root)
print()

# Count nodes
total = count_nodes(root)
print(f"\nTotal number of nodes: {total}")



























