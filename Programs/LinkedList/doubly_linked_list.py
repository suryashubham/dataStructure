class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


Head = None


def create_doubly_linked_list(prev_node=None):
    global Head
    k = input('do you want to enter a node?(y/Y)->')
    if k == ('y' or 'Y'):
        p = input('enter a node value-->')
        node = Node(p)
        if Head is None:
            Head = node
        else:
            prev_node.next = node
            node.prev = prev_node
        create_doubly_linked_list(node)
    return Head
