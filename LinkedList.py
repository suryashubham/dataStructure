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

def reverse_linked_list(calling_node, head):
    if head:
        reverse_linked_list(head, head.link)
        head.link = calling_node
    else:
        global Head
        Head = calling_node
    return

def print_ll(head):
    if head:
        print(head.data)
        print_ll(head.link)
    return


h = create_linked_list()
reverse_linked_list(None, Head)
print_ll(Head)
