#TC--->0(n)
v_dict = {}

def vertical_order(root, level):
    if root:
        if level not in v_dict:
            v_dict[level] = []
        v_dict[level].append(root.data)
        vertical_order(root.left, level - 1)
        vertical_order(root.right, level + 1)
    return
