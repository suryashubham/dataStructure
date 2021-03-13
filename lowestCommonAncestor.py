#lowest common ancestor in a binary tree --- Leetcode challenge solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        n1=self.lowestCommonAncestor(root.left, p, q)
        n2= self.lowestCommonAncestor(root.right, p, q)
        if n1 and n2:
            return root
        return n1 if n1 else n2
      
      #i/p-- 
#       [3,5,1,6,2,0,8,null,null,7,4]
#       5
#       4
     
