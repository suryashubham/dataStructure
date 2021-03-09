#delete a node of a single linked list passed as input by user
def delete_node(head, current_node, next_node, k):
    if head is None:
        return
    if head.data == k:
        head = head.link
        return head
    if next_node.data == k:
        current_node.link = next_node.link
        next_node.link = None
        return
    delete_node(head, current_node.link, next_node.link, k)
