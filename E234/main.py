class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


def reverseList(head):
    if not head or not head.next:
        return head, 1

    prev = None
    cur = head
    n = 0
    while cur:
        n += 1
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev, n


def copyList(node):
    dummy = current = ListNode(0)
    while node:
        current.next = ListNode(node.val)
        current = current.next
        node = node.next
    return dummy.next


class Solution(object):

    def isPalindrome(self, head):
        front = head
        back, n = reverseList(copyList(head))
        for _ in range(n // 2):
            print(front.val, back.val)
            if front.val != back.val:
                return False
            front = front.next
            back = back.next
        return True


solution = Solution()
node = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(solution.isPalindrome(node))
