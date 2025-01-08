# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate
            else:
                current = current.next  # Move to the next node
        
        return head