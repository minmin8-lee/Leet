# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ListNode case
        if l1 is not None and l2 is not None:
            M, m = self._node_compare_(l1, l2)
            head = ListNode(m.val)
            m = m.next
            cursor = head

            while m is not None:
                M, m = self._node_compare_(m, M)
                cursor.next = ListNode(m.val)
                cursor = cursor.next
                m = m.next

            # for safe copy, copy all
            while M is not None:
                cursor.next = ListNode(M.val)
                cursor = cursor.next
                M = M.next

            return head

        # if ~ListNode case
        else:
            if l1 is not None:
                return l1
            else:
                return l2

    @staticmethod
    def _node_compare_(a: ListNode, b: ListNode):
        if a.val >= b.val:
            return a, b
        else:
            return b, a
