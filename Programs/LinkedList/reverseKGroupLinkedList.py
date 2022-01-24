class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        next_ptr=prev_ptr=None
        cur_ptr = head
        c=0
        while cur_ptr and c<k:
            next_ptr = cur_ptr.next
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = next_ptr
            c=c+1
        if next_ptr:
            head.next = self.reverseKGroup(next_ptr,k)
        return prev_ptr
        
