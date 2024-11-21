# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addTwoNumbersHelper(l1,l2, carry_in):
            if l1 and l2:
                digit = l1.val+l2.val+carry_in
                carry_out = digit//10
                digit = digit%10              
                l = ListNode(digit, None)
                l.next = addTwoNumbersHelper(l1.next, l2.next, carry_out)
                return l
            elif l1:
                if carry_in :
                    digit = l1.val+carry_in
                    carry_out = digit//10
                    digit = digit%10              
                    l = ListNode(digit, None)
                    l.next = addTwoNumbersHelper(l1.next, None, carry_out)
                    return l
                return l1
            elif l2:
                if carry_in :
                    digit = l2.val+carry_in
                    carry_out = digit//10
                    digit = digit%10              
                    l = ListNode(digit, None)
                    l.next = addTwoNumbersHelper(None, l2.next, carry_out)
                    return l
                return l2
            else:
                if carry_in:
                    digit = carry_in
                    carry_out = digit//10
                    digit = digit%10              
                    l = ListNode(digit, None)
                    l.next = addTwoNumbersHelper(None, None, carry_out)
                    return l
                return None
        return addTwoNumbersHelper(l1,l2,0)