class NewNode:
    def __init__(self, root=None):
        self.data = root
        self.left = self.right = None


arr = [5, 3, 6, 2, 4]


def construct_binary_tree(index):
    root = None
    if index < len(arr):
        root = NewNode(arr[index])
        root.left = construct_binary_tree(2 * index + 1)
        root.right = construct_binary_tree(2 * index + 2)
    return root


def construct_mirror_tree(r):
    if r is None:
        return
    else:
        construct_mirror_tree(r.left)
        construct_mirror_tree(r.right)
        temp_node = NewNode()
        temp_node = r.left
        r.left = r.right
        r.right = temp_node


def inorder(r):
    if r:
        inorder(r.left)
        print(r.data, end='')
        inorder(r.right)


if __name__ == '__main__':
    root_node = construct_binary_tree(0)
    inorder(root_node)
    print()
    construct_mirror_tree(root_node)
    inorder(root_node)
