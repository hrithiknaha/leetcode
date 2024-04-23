# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev1, curr, length_one = None, l1, 0

        while curr:
            next = curr.next
            curr.next = prev1
            prev1 = curr
            curr = next
            length_one += 1
        
        prev2, curr, length_two = None, l2, 0

        while curr:
            next = curr.next
            curr.next = prev2
            prev2 = curr
            curr = next
            length_two += 1
        
        number1 = 0

        while prev1:
            number1 = prev1.val * pow(10, length_one - 1) + number1
            prev1 = prev1.next
            length_one -=1
        
        number2 = 0

        while prev2:
            number2 = prev2.val * pow(10, length_two - 1) + number2
            prev2 = prev2.next
            length_two -= 1
        
        result = number1 + number2

        if result == 0:
            return ListNode()

        dummy_node = ListNode()
        curr = dummy_node

        while result > 0:
            digit = result % 10
            new_node = ListNode(digit)
            curr.next = new_node
            curr = curr.next

            result = result // 10
        
        return dummy_node.next

            




        
