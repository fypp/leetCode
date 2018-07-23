# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        value_list = []
        for node in lists:
            if node:
                value_list.append(node.val)
                node_next = node.next
                while node_next:
                    value_list.append(node_next.val)
                    node_next = node_next.next
        if len(value_list) == 0:
            return None
        elif len(value_list) == 1:
            return ListNode(value_list[0])
        result_list = sorted(value_list)

        node_now = ListNode(result_list[len(result_list) - 1])
        for i in range(len(result_list) - 1, 0, -1):
            result_list[i - 1] = ListNode(result_list[i - 1])
            result_list[i - 1].next = node_now
            node_now = result_list[i - 1]

        result = result_list[0]
        return result

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result_list = []
        while head:
            result_list.append(head.val)
            head = head.next
        result_list = sorted(result_list)
        if len(result_list) == 0:
            return None
        elif len(result_list) == 1:
            return ListNode(result_list[0])
        node_now = ListNode(result_list[len(result_list) - 1])
        for i in range(len(result_list) - 1, 0, -1):
            result_list[i - 1] = ListNode(result_list[i - 1])
            result_list[i - 1].next = node_now
            node_now = result_list[i - 1]

        result = result_list[0]
        return result

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        node = head
        # 插入原节点的next
        while node:
            tmp = RandomListNode(node.label)
            tmp.next = node.next
            node.next = tmp
            node = tmp.next

        # 获取新节点的random
        node = head
        while node and node.next:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # 截取新节点
        head_new = head.next
        old = head
        node = head.next
        while old:
            old.next = old.next.next
            if node.next:
                node.next = node.next.next
            node = node.next
            old = old.next
        return head_new


