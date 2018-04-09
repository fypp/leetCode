# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_next = node.next
        node.val = node_next.val
        node.next = node_next.next

    def next_n_node(self, node, n):
        for i in range(n + 1):
            if node is None:
                return True
            node = node.next
        return False

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        if node.next is None and n == 1:
            return None
        if self.next_n_node(head, n):
            head = head.next
            return head

        while not self.next_n_node(node, n + 1):
            node = node.next
        node.next = node.next.next
        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = []
        node = head
        if node is None:
            return None
        if node.next is None:
            return head
        while node:
            result.append(node)
            node = node.next
        result[0].next = None
        for i in range(1, len(result)):
            result[-1 * i].next = result[-1 * i - 1]
        return result[len(result) - 1]

    def compareNode(self, n1, n2):
        if n1 is None:
            return None, n2
        if n2 is None:
            return None, n1
        if n1.val < n2.val:
            return n1, n2
        else:
            return n2, n1

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node_min, node_max = self.compareNode(l1, l2)
        result_node = ListNode(node_min.val)
        node_next = result_node
        while node_min is not None:
            node_next.next = ListNode(node_min.val)
            node_min, node_max = self.compareNode(node_min.next, node_max)
            node_next = node_next.next
        node_next.next = node_max
        return result_node.next

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        for i in range(len(result)//2):
            if result[i] != result[-1*(i+1)]:
                return False
        return True

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = {}
        node = head
        while node:
            if node in nodes:
                return True
            else:
                nodes[node] = 1
            node = node.next
        return False
