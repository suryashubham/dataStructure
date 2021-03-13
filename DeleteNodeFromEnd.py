# deleting k'th node of a LL from end. TC---> 0(n)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev_ptr = None
        fast_ptr=slow_ptr=head
        lastNode = True
        
        for _ in range(n-1):
            fast_ptr = fast_ptr.next
            lastNode = False
        
        while fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        if fast_ptr == slow_ptr and prev_ptr is None:
            return None
        elif prev_ptr:
            prev_ptr.next = slow_ptr.next
            slow_ptr.next = None
        else:
            x = slow_ptr.next
            slow_ptr.next = prev_ptr
            return x
        return head
