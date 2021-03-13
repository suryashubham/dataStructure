# swapping k'th node from beginning with the k'th node from end of a linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast_ptr, slow_ptr = head,head
        
        for _ in range(k-1):
            fast_ptr=fast_ptr.next
        
        first = fast_ptr
        
        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
            
        first.val,slow_ptr.val=slow_ptr.val,first.val
        return head
