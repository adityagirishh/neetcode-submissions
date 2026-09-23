# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
            while (head.next != None and head.val<head.next.val):
                head = head.next
            if(head.next != None and head.val>head.next.val):
                return True
            if(head.next == None):
                return False
            return True