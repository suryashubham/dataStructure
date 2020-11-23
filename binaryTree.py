class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


arr = [1, 2, 3, 4, 5, 6]
q = []
dia = 0


def create_level_order_binary_tree(i):
    root = None
    if i < len(arr):
        root = NewNode(arr[i])
        root.left = create_level_order_binary_tree(2 * i + 1)
        root.right = create_level_order_binary_tree(2 * i + 2)
    return root


def preorder(root):
    if root:
        print(root.data, end='')
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end='')
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='')


def levelOrder(root):
    if root:
        if len(q) > 0:
            del q[0]
        print(root.data, end='')
        q.append(root.left)
        q.append(root.right)
        levelOrder(q[0])


def total_nodes(root):
    if root:
        return 1 + total_nodes(root.left) + total_nodes(root.right)
    else:
        return 0


def number_of_leafs(root):
    if root is None:
        return 0
    if root and root.left == root.right is None:
        return 1
    else:
        return number_of_leafs(root.left) + number_of_leafs(root.right)


def total_full_nodes(root):
    if root is None:
        return 0
    elif root.left is not None and root.right is not None:
        return 1 + total_full_nodes(root.left) + total_full_nodes(root.right)
    else:
        return 0


def total_non_leaf_nodes(root):
    if root is None:
        return 0
    elif root.left is not None or root.right is not None:
        return 1 + total_non_leaf_nodes(root.left) + total_non_leaf_nodes(root.right)
    else:
        return 0
  
def height_of_tree(root):
    if root is None:
        return 0
    if root.left == root.right is None:
        return 0
    if root:
        left_ht = height_of_tree(root.left)
        right_ht = height_of_tree(root.right)
        return 1 + max(left_ht, right_ht)
  
def diameter(root):
    global dia
    if root is None:
        return 0
    if root.left == root.right is None:
        return 1
    if root:
        left = diameter(root.left)
        right = diameter(root.right)
        if left + right > dia:
            dia = left + right
        return left + right


if __name__ == "__main__":
    root_node = create_level_order_binary_tree(0)
    preorder(root_node)
    print()
    inorder(root_node)
    print()
    postorder(root_node)
    print()
    levelOrder(root_node)
    print()
    len = total_nodes(root_node)
    print("total no. of nodes:" + str(len))
    leaf_nodes = number_of_leafs(root_node)
    print("number of leaf nodes:" + str(leaf_nodes))
    full_nodes = total_full_nodes(root_node)
    print("number of full nodes:" + str(full_nodes))
    no_leaf_node = total_non_leaf_nodes(root_node)
    print("number of non-leaf nodes:" + str(no_leaf_node))
    height = height_of_tree(root_node)
    print("height of tree:" + str(height))
     d = diameter(root_node)
    print("diameter of tree is:", dia)
