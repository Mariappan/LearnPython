# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = last = None
        remainder = 0
        
        while l1 is not None or l2 is not None:
            temp = ListNode(0)
            if l1 is not None:
                temp.val = temp.val + l1.val
                
            if l2 is not None:
                temp.val = temp.val + l2.val
                
            temp.val = temp.val + remainder
            
            remainder = temp.val // 10
            temp.val = temp.val % 10
            
            if last is not None:
                last.next = temp 
                last = temp
            else:
                result = temp
                last = temp
            
            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
        
        if 1 == remainder:
            last.next = ListNode(1)
            
        return result
