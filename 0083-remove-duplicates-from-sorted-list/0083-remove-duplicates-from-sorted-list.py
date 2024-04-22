# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
            
        curr = head
        first_head = curr

        while head != None:
            if curr.val == head.val:
                head = head.next
            else:
                curr.next = head
                curr = head
        
        curr.next = None

        return first_head
        

        