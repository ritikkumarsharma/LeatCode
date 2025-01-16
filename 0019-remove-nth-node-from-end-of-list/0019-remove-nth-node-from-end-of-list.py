# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while head:
            c +=1
            head = head.next
        if n == c:
            return temp.next
        head = temp
        n = c - n
        while n != 1:
            n -= 1
            head = head.next
        head.next = head.next.next
        return temp