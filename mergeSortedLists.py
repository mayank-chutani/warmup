# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        head = None
        if (l1 is None):
            return l2
        elif (l2 is None):
            return l1
        ptr1 = l1 if l1.val <= l2.val else l2
        ptr2 = l1 if l1.val > l2.val else l2
        next1 = ptr1.next
        next2 = ptr2.next

        head = ptr1

        while (next1):
            if (ptr1.val <= ptr2.val and ptr2.val <= next1.val):
                ptr1.next = ptr2
                ptr2.next = next1
                ptr2 = next2
                if (ptr2 is None):
                    break
                next1 = ptr1.next
                next2 = ptr2.next
            else:
                ptr1 = ptr1.next
                next1 = next1.next

        if (ptr2):
            ptr1.next = ptr2
        return head

# # IDEA:
1. ptr1 always points to the smallest first element list
2. initialise the next pointers
3. insert all elements from list2 which fit between ptr1 and next1
4. then move forward
