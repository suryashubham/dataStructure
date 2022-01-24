class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def create_level_order_binary_tree(i):
    root = None
    if i < len(arr):
        root = NewNode(arr[i])
        root.left = create_level_order_binary_tree(2 * i + 1)
        root.right = create_level_order_binary_tree(2 * i + 2)
    return root


def find_the_level(root, n, l):
    if root is None:
        return -1
    if root.data == n:
        return l
    x = find_the_level(root.left, n, l + 1)
    if x != -1:
        return x
    else:
        y = find_the_level(root.right, n, l + 1)
        return y


if __name__ == "__main__":
    root_node = create_level_order_binary_tree(0)
    k = find_the_level(root_node, 12, 0)
    print(k)
