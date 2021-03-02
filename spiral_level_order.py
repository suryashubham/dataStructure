def traverse_spiral_order(root, level, arr):
    if root:
        if level % 2 == 0:
            if level < len(arr):
                arr[level].append(root.data)
            else:
                arr.append([])
                arr[level].append(root.data)
        else:
            if level < len(arr):
                arr[level].insert(0, root.data)
            else:
                arr.append([])
                arr[level].insert(0, root.data)
        traverse_spiral_order(root.left, level + 1, arr)
        traverse_spiral_order(root.right, level + 1, arr)
    return arr
