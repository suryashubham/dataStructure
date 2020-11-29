# create a level order binary tree and traverse it vertically.

vertical_maximum = 0
vertical_minimum = 0


class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
q = []
dia = 0


def create_level_order_binary_tree(i):
    root = None
    if i < len(arr):
        root = NewNode(arr[i])
        root.left = create_level_order_binary_tree(2 * i + 1)
        root.right = create_level_order_binary_tree(2 * i + 2)
    return root


def vertical_order(root, val):
    global vertical_maximum
    global vertical_minimum
    if root is None:
        return
    if val > vertical_maximum:
        vertical_maximum = val
    if val < vertical_minimum:
        vertical_minimum = val
    vertical_order(root.left, val - 1)
    vertical_order(root.right, val + 1)


def traverse_vertically(root, val, match):
    if root is None:
        return
    if val == match:
        print(root.data, end=' ')
    traverse_vertically(root.left, val - 1, match)
    traverse_vertically(root.right, val + 1, match)


if __name__ == "__main__":
    root_node = create_level_order_binary_tree(0)
    vertical_order(root_node, 0)
    for x in range(vertical_minimum, vertical_maximum + 1):
        traverse_vertically(root_node, 0, x)
