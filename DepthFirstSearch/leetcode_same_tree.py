class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None :
            return True 
        else:
            return False     

        left_status = self.isSameTree(p.left, q.left)
        right_status = self.isSameTree(p.right, q.right)
        
        if left_status :
            return True 

        if right_status:
            return False    

            

    
