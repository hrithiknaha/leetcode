# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB

        length_a = 0
        length_b = 0

        while headA:
            length_a += 1
            headA = headA.next

        while headB:
            length_b += 1
            headB = headB.next

        while length_a - length_b > 0:
            currA = currA.next
            length_a -= 1
        
        while length_b - length_a > 0:
            currB = currB.next
            length_b -= 1
        
        while currA and currB:
            if currA == currB:
                return currA
            
            currA = currA.next
            currB = currB.next
        
        return None