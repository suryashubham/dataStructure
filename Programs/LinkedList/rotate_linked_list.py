def rotate_linked_list(head, k):
    cur_ptr = head
    prev_ptr = None
    len_ll = 0

    if head is None:
        return -1
    while cur_ptr:
        len_ll += 1
        prev_ptr = cur_ptr
        cur_ptr = cur_ptr.next

    last_node = prev_ptr
    new_k = k % len_ll if k > len_ll else k
    if new_k == len_ll or new_k == 0:
        return head
    return rotate(len_ll, new_k, head, last_node)


def rotate(len_ll, k, head, last_node):
    skips = len_ll - k
    tn = head
    for i in range(1, skips):
        tn = tn.next
    cut_node = tn.next
    tn.next = None
    last_node.next = head
    head = cut_node
    return head
