class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


solution = Solution()
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(solution.reverseList(node))
