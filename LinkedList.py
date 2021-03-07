class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


Head = None

def create_linked_list(n=None):
    global Head
    k = input('do you want to enter a node?(y/Y)->')
    if k == ('y' or 'Y'):
        p = input('enter a node value-->')
        node = Node(p)
        if Head is None:
            Head = node
        else:
            n.link = node
        create_linked_list(node)
    return Head


def print_ll(head):
    if head:
        print(head.data)
        print_ll(head.link)
    return


h = create_linked_list()
print_ll(h)
