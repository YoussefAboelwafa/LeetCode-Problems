class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):

        # point cur to list1
        cur = list1
        for _ in range(0, a - 1):
            cur = cur.next

        # point tail to list2
        tail = cur.next

        # point tail to the end of list2
        for _ in range(b - a + 1):
            tail = tail.next

        # point cur to list2
        cur.next = list2

        # point cur to the end of list2
        while cur.next:
            cur = cur.next

        # point cur to tail
        cur.next = tail

        return list1


solution = Solution()

list1 = ListNode(0)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(4)
list1.next.next.next.next.next = ListNode(5)
list1.next.next.next.next.next.next = ListNode(6)


list2 = ListNode(1000000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)
list2.next.next.next = ListNode(1000003)
list2.next.next.next.next = ListNode(1000004)

print(
    solution.mergeInBetween(list1, 2, 5, list2)
)  # 0->1->1000000->1000001->1000002-> 6
