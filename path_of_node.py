class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


arr = [1, 2, 3, 4, 5, 6, 7]
q = []


def create_level_order_binary_tree(i):
    root = None
    if i < len(arr):
        root = NewNode(arr[i])
        root.left = create_level_order_binary_tree(2 * i + 1)
        root.right = create_level_order_binary_tree(2 * i + 2)
    return root


# def preorder(root):
#     if root:
#         print(root.data, end='')
#         preorder(root.left)
#         preorder(root.right)
#
#
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end='')
#         inorder(root.right)
#
#
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data, end='')
#
#
# def levelOrder(root):
#     if root:
#         if len(q) > 0:
#             del q[0]
#         print(root.data, end='')
#         q.append(root.left)
#         q.append(root.right)
#         levelOrder(q[0])
#
#
# def total_nodes(root):
#     if root:
#         return 1 + total_nodes(root.left) + total_nodes(root.right)
#     else:
#         return 0
#
#
# def number_of_leafs(root):
#     if root is None:
#         return 0
#     if root and root.left == root.right is None:
#         return 1
#     else:
#         return number_of_leafs(root.left) + number_of_leafs(root.right)
#
#
# def total_full_nodes(root):
#     if root is None:
#         return 0
#     elif root.left is not None and root.right is not None:
#         return 1 + total_full_nodes(root.left) + total_full_nodes(root.right)
#     else:
#         return 0
#
#
# def total_non_leaf_nodes(root):
#     if root is None:
#         return 0
#     elif root.left is not None or root.right is not None:
#         return 1 + total_non_leaf_nodes(root.left) + total_non_leaf_nodes(root.right)
#     else:
#         return 0


def dfs(root, p, temp_path, path):
    #print(temp_path)
    if root is None:
        return path
    if root.data == p:
        if len(temp_path) == 0:
            path.append(root.data)
            return path
        else:
            temp_path.append(root.data)
            path.append(temp_path)
            return path
    temp_path.append(root.data)
    # print(temp_path)
    # print()
    path = dfs(root.left, 6, temp_path, path)
    if len(path) == 0:
        path = dfs(root.right, 6, temp_path, path)
    return path


if __name__ == "__main__":
    root_node = create_level_order_binary_tree(0)
    # t_p = list()
    # p = list()
    # preorder(root_node)
    # print()
    # inorder(root_node)
    # print()
    # postorder(root_node)
    # print()
    # levelOrder(root_node)
    # print()
    # len = total_nodes(root_node)
    # print("total no. of nodes:" + str(len))
    # leaf_nodes = number_of_leafs(root_node)
    # print("number of leaf nodes:" + str(leaf_nodes))
    # full_nodes = total_full_nodes(root_node)
    # print("number of full nodes:" + str(full_nodes))
    # no_leaf_node = total_non_leaf_nodes(root_node)
    # print("number of non-leaf nodes:" + str(no_leaf_node))
    k = dfs(root_node, 6, [], [])
    print(k)

