"""
和删除链表的节点一样
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        p=ans
        while p and p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next

        return ans.next