# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Given an linked list of two numbers in reverse order, add the two numbersSearch (arr, start, end, elem):
    Mid = 1 + (len(arr) - 1)/2
    if(arr[mid] == elem):
        Return True
    if(arr[start] <= arr[mid]):
        if (elem >= arr[start] and elem <= arr[mid]):
            Return search(arr, start, mid-1, elem)
        Return search(arr, mid+1, end, elem)

    If (elem >= arr[mid] and elem <= arr[end]):
        Return search(arr, mid+1, end, elem)

    Return search(arr, start, mid-1, elem)
.

class Solution:

    def add(self, val1, val2, carr):
        carry = 0
        val = val1 + val2 + carr
        if (val > 9):
            carry = int(val / 10)
            val = int(val % 10)
        return val, carry

    def addToLL(self, result, addition, curr):
        if (result is None):
            result = ListNode(addition)
            curr = result
        else:
            curr.next = ListNode(addition)
            curr = curr.next
        return curr, result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        if (l1 is None):
            return l2
        elif (l2 is None):
            return l1

        result = None
        curr = None
        val1 = l1.val
        val2 = l2.val
        while(True):
            addition, carry = self.add(val1, val2, carry)
            curr, result = self.addToLL(result, addition, curr)
            if (l1.next is None and l2.next is None):
                if (carry > 0):
                    curr.next = ListNode(carry)
                break

            if (l1.next is not None):
                l1 = l1.next
                val1 = l1.val
            else:
                val1 = 0
            if (l2.next is not None):
                l2 = l2.next
                val2 = l2.val
            else:
                val2 = 0
        return result
