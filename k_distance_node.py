#find all the nodes which are at a distance 'k'(distance provided by user) from root node

def find_nodes_at_distance_k_from_root_node(root, base_index, required_index):
    if root is None:
        return
    if root:
        if base_index == required_index:
            print(root.data, end='')
            return
        else:
            find_nodes_at_distance_k_from_root_node(root.left, base_index + 1, required_index)
            find_nodes_at_distance_k_from_root_node(root.right, base_index + 1, required_index)
            return
