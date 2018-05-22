# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root is None):
            return None
        if (root.val == p.val):
            if ( self.findKey(root.left, q) or self.findKey(root.right, q) ):
                return root
            else:
                return None
        elif (root.val == q.val):
            if ( self.findKey(root.left, p) or self.findKey(root.right, p) ):
                return root
            else:
                return None

        left = None
        right = None
        if (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            if (self.findKey(root, p) and self.findKey(root, q)):
                return root
            else:
                return None


    def findKey(self, root, key):
        if root is None:
            return None
        if root.val == key.val:
            return True
        if key.val < root.val:
            return self.findKey(root.left, key)
        else:
            return self.findKey(root.right, key)

        
