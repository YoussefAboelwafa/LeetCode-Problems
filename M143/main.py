class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


def reverseList(head):
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


class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        start = slow = fast = head
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        slow_prev.next = None

        rev = reverseList(slow)

        cur1 = start
        cur2 = rev

        while cur1.next and cur2.next:
            nxt1 = cur1.next
            nxt2 = cur2.next
            cur1.next = cur2
            cur2.next = nxt1
            cur1 = nxt1
            cur2 = nxt2

        cur1.next = cur2


solution = Solution()
head = ListNode(1)
solution.reorderList(head)
