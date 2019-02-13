# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll = ListNode(0)
        cur = ll
        ext = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + ext
            t = sum % 10
            ext = sum / 10
            l = ListNode(t)
            cur.next = l
            cur = l
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            sum = l1.val + ext
            t = sum % 10
            ext = sum / 10
            l = ListNode(t)
            cur.next = l
            cur = l
            l1 = l1.next
        while l2 is not None:
            sum = l2.val + ext
            t = sum % 10
            ext = sum / 10
            l = ListNode(t)
            cur.next = l
            cur = l
            l2 = l2.next
        if ext != 0:
            l = ListNode(ext)
            cur.next = l
        return ll.next


l1 = ListNode(2)
n1 = ListNode(4)
n2 = ListNode(3)
n1.next = n2
l1.next = n1

l2 = ListNode(5)
n1 = ListNode(6)
n2 = ListNode(4)
n1.next = n2
l2.next = n1

ll = Solution().addTwoNumbers(ListNode(5), ListNode(5))
while ll is not None:
    print ll.val
    ll = ll.next
