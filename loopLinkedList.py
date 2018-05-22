# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None or head.next is None):
            return False

        ptr = head
        f_ptr = head.next

        while True:
            if (ptr == f_ptr):
                return True

            if (ptr is None or f_ptr is None or f_ptr.next is None):
                return False

            ptr = ptr.next
            f_ptr = f_ptr.next.next


        
