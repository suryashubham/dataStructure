class CreateNode:
    def __init__(self, arr, mid):
        self.data = arr[mid]
        self.left = self.right = None


def create_bst(arr, left, right):
    if left <= right:
        mid = int((left + right) / 2)
        # print(mid)
        root = CreateNode(arr, mid)
        root.left = create_bst(arr, left, mid - 1)
        root.right = create_bst(arr, mid + 1, right)
        return root
    else:
        return None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end='')
        inorder(root.right)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
node = create_bst(array, 0, len(array) - 1)
inorder(node)
