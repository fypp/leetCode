class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1

        count = 0
        node = self
        while node:
            if index == count:
                res = node.val if node.val is not None else -1
                return res
            node = node.next
            count += 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = MyLinkedList()
        node.val = self.val
        node.next = self.next
        if node.val is None:
            node = None
        self.val = val
        self.next = node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = self
        while node.next:
            node = node.next
        last_node = MyLinkedList()
        last_node.val = val
        node.next = last_node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        node_cur = MyLinkedList()
        node_cur.val = val

        count = 0
        node = self if self.val is not None else None

        if index == 0:
            self.addAtHead(val)

        while count < index and node is not None:
            node_pre = node
            node_next = node.next
            count += 1
            if count == index:
                node_cur.next = node_next
                node_pre.next = node_cur
                return
            node = node.next

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        count = 0
        node = self

        while node.next:
            node_pre = node
            node_next = node.next
            count += 1
            if count == index:
                node_pre.next = node_next.next
                return
            if node_next is None:
                node_pre.next = None
                return
            node = node.next

class MyLinkedList2(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1

        count = 0
        node = self
        while node:
            if index == count:
                res = node.val if node.val is not None else -1
                return res
            node = node.next
            count += 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = MyLinkedList()
        node.val = self.val
        node.next = self.next
        if node.val is None:
            node = None
        self.val = val
        self.next = node


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = self
        while node.next:
            node = node.next
        last_node = MyLinkedList()
        last_node.val = val
        node.next = last_node


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        node_cur = MyLinkedList()
        node_cur.val = val

        count = 0
        node = self if self.val is not None else None

        if index == 0:
            self.addAtHead(val)

        while count < index and node is not None:
            node_pre = node
            node_next = node.next
            count += 1
            if count == index:
                node_cur.next = node_next
                node_pre.next = node_cur
                return
            node = node.next




    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        count = 0
        node = self

        while node.next:
            node_pre = node
            node_next = node.next
            count += 1
            if count == index:
                node_pre.next = node_next.next
                return
            if node_next is None:
                node_pre.next = None
                return
            node = node.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node_in_cycle = None
        node_quick = head
        node_normal = head
        while node_quick:
            if node_quick.next is None:
                return None
            node_quick = node_quick.next.next
            node_normal = node_normal.next
            if node_quick == node_normal:
                node_in_cycle = node_quick
                break

        if node_in_cycle is None:
            return None

        node_begin = head
        while node_begin != node_in_cycle:
            node_begin = node_begin.next
            node_in_cycle = node_in_cycle.next
        return node_begin

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)

        node_pre = head
        node = head.next

        while node:
            if node.val == val:
                node = node.next
                node_pre.next = node
            else:
                node = node.next
                node_pre = node_pre.next
        return head

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        node = head
        while node:
            if node.child:
                node_child = self.flatten(node.child)
                node.child = None
                node_child.prev = node
                node_tmp = node_child
                while node_tmp.next:
                    node_tmp = node_tmp.next
                node_tmp.next = node.next
                if node.next:
                    node.next.prev = node_tmp
                node.next = node_child
                node = node_tmp.next
            else:
                node = node.next

        return head

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k<0:
            return None

        if k == 0:
            return head



        total = 1
        node_last = None

        # 获取总节点个数
        node = head
        while node.next:
            total += 1
            node_last = node.next
            node = node.next

        p = total - k % total
        if total == 1 or p==total:
            return head


        # 获取最后一个节点
        inx = 1
        node_p = head
        while inx < p:
            inx += 1
            node_p = node_p.next

        # 生成新链表
        node_first = node_p.next
        node_p.next = None
        node_last.next = head
        return node_first

