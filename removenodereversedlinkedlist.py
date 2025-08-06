# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        nr=0
        head_copy=head
        while head_copy:
            head_copy=head_copy.next
            nr += 1
        print(nr)
        if nr == n:
            return head.next

        current = head
        for i in range(1, nr-n):
            current = current.next
        current.next = current.next.next
        return head