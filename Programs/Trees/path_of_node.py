from copy import deepcopy
class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
q = []


def create_level_order_binary_tree(i):
    root = None
    if i < len(arr):
        root = NewNode(arr[i])
        root.left = create_level_order_binary_tree(2 * i + 1)
        root.right = create_level_order_binary_tree(2 * i + 2)
    return root


def path(root, p, temp_path):
    if root:
        # temp_path = temp_path + str(root.data)
        # temp_path = temp_path + "->"
        temp_path.append(root.data)
    if root is None:
        return
    if root.data == p:
        return temp_path
    x = path(root.left, 14, deepcopy(temp_path))
    if x is not None:
        return x
    else:
        return path(root.right, 14, deepcopy(temp_path))
#     commented code below is also an alternative but the above one is the better approach
#     y = path(root.right, 14, deepcopy(temp_path))
#     if x:
#         return x
#     else:
#         return y

if __name__ == "__main__":
    root_node = create_level_order_binary_tree(0)
    k = path(root_node, 14, [])
    print(k)
