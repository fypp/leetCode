# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inOrderTravel(self, root):
        nodes = []
        if root:
            if root.left:
                nodes += self.inOrderTravel(root.left)
            nodes.append(root.val)
            if root.right:
                nodes += self.inOrderTravel(root.right)
        return nodes

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = self.inOrderTravel(root)
        if len(nodes) < 2:
            return True
        node_init = nodes[0]
        for node in nodes[1:]:
            if node <= node_init:
                return False
            node_init = node
        return True

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if root.val == val:
                return root
            if root.val < val:
                return self.searchBST(root.right, val)
            if root.val > val:
                return self.searchBST(root.left, val)
        return None

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if root.val < val:
                if root.right:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
            if root.val > val:
                if root.left:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            if root.val == val:
                return None
        else:
            root = TreeNode(val)
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root:
            if root.val < key:
                if root.right:
                    root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                if root.left:
                    root.left = self.deleteNode(root.left, key)
            elif root.val == key:
                if root.left and not root.right:
                    root = root.left
                elif root.right and not root.left:
                    root = root.right
                elif not root.left and not root.right:
                    root = None
                elif root.left and root.right:
                    node = root.right
                    while node.left:
                        node = node.left
                    node.right = self.deleteNode(root.right, node.val)
                    node.left = root.left
                    root = node

        return root

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            val_diff_p = root.val - p.val
            val_diff_q = root.val - q.val
            if val_diff_p * val_diff_q <= 0:
                return root
            else:
                if val_diff_p > 0:
                    return self.lowestCommonAncestor(root.left, p, q)
                else:
                    return self.lowestCommonAncestor(root.right, p, q)
        else:
            return None

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0 or len(nums) < 2:
            return False

        import collections
        orderDict = collections.OrderedDict()
        for i in range(len(nums)):
            rates = nums[i] // max(t, 1)
            for rate in (rates-1, rates, rates+1):
                if rate in orderDict and abs(nums[i] - orderDict[rate]) <= t:
                        return True
            orderDict[rates] = nums[i]
            if i >= k:
                orderDict.popitem(last=False)
        return False

    def getDepth(self, root):
        if root:
            if root.left:
                depth_left = self.getDepth(root.left) + 1
            else:
                depth_left = 1
            if root.right:
                depth_right = self.getDepth(root.right) + 1
            else:
                depth_right = 1
        else:
            return 0
        return max(depth_left, depth_right)



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            depth_left = self.getDepth(root.left)
            depth_right = self.getDepth(root.right)
            if abs(depth_left-depth_right) > 1:
                return False
            if not self.isBalanced(root.left):
                return False
            if not self.isBalanced(root.right):
                return False
        return True

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        elif len(nums)==2:
            node_left = TreeNode(nums[0])
            node_root = TreeNode(nums[1])
            node_root.left = node_left
            return node_root
        median_inx = len(nums)//2
        root = TreeNode(nums[median_inx])
        root.left = self.sortedArrayToBST(nums[:median_inx])
        root.right = self.sortedArrayToBST(nums[median_inx+1:])
        return root




node31 = TreeNode(15)
node32 = TreeNode(7)
node21 = TreeNode(9)
node22 = TreeNode(20)
node22.left = node31
node22.right = node32
node1=TreeNode(3)
node1.left=node21
node1.right=node22

Solution().isBalanced(node1)

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeftNode(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.pushLeftNode(node.right)
        return node.val

    def pushLeftNode(self, root):
        while root:
            self.stack.append(root)
            root = root.left


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)
        if len(nums) > k:
            self.nums = self.nums[0:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if self.k != len(self.nums):
            self.nums.pop()
        return self.nums[-1]
