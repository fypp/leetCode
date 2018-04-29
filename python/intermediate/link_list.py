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
        list_l1 = [l1.val]
        list_l2 = [l2.val]
        while l1.next:
            list_l1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            list_l2.append(l2.next.val)
            l2 = l2.next
        num_l1 = int("".join([str(x) for x in list_l1[::-1]]))
        num_l2 = int("".join([str(x) for x in list_l2[::-1]]))
        num_list = list(str(num_l1 + num_l2))
        node_list = [ListNode(num_list[0])]
        for i in range(1, len(num_list)):
            node = ListNode(num_list[i])
            node_list.append(node)
            node_list[i].next = node_list[i - 1]
        return node_list[-1]

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        head_even = head.next
        node_odd = head
        node_even = head_even
        while node_even and node_even.next:
            node_odd.next = node_even.next
            node_odd = node_even.next
            node_even.next = node_odd.next
            node_even = node_odd.next
        node_odd.next = head_even
        return head

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA and pB and pA != pB:
            pA = pA.next
            pB = pB.next
            if pA == pB:
                return pA
            if not pA:
                pA = headB
            if not pB:
                pB = headA
        return pA
