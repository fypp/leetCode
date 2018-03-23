# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if root is None:
            return result

        if isinstance(root, TreeNode):
            result.append(root.val)
            if root.left is not None:
                result += Solution().preorderTraversal(root.left)
            if root.right is not None:
                result += Solution().preorderTraversal(root.right)
        else:
            result.append(root)
        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if root is None:
            return result

        if isinstance(root, TreeNode):
            if root.left is not None:
                result += Solution().inorderTraversal(root.left)
            result.append(root.val)
            if root.right is not None:
                result += Solution().inorderTraversal(root.right)
        else:
            result.append(root)
        return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if root is None:
            return result

        if isinstance(root, TreeNode):
            if root.left is not None:
                result += Solution().postorderTraversal(root.left)
            if root.right is not None:
                result += Solution().postorderTraversal(root.right)
            result.append(root.val)
        else:
            result.append(root)
        return result

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if root is None:
            return result

        nodes, node_child = [root], []
        while nodes:
            node_row = []
            for node in nodes:
                node_row.append(node.val)
                if node.left is not None:
                    node_child.append(node.left)
                if node.right is not None:
                    node_child.append(node.right)

            nodes, node_child = node_child, []
            result.append(node_row)
        return result

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = True

        def twoNodeSymmetric(left_node, right_node):

            if left_node is None:
                if right_node is not None:
                    self.result = False
            elif right_node is None:
                self.result = False
            elif left_node.val != right_node.val:
                self.result = False
            else:
                twoNodeSymmetric(left_node.left, right_node.right)
                twoNodeSymmetric(left_node.right, right_node.left)

        if root is None:
            return True

        twoNodeSymmetric(root.left, root.right)
        return self.result

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        result_left, result_right = False, False
        if (sum == root.val) & (root.left is None) & (root.right is None):
            return True
        if root.left is not None:
            result_left = self.hasPathSum(root.left, sum - root.val)
        if root.right is not None:
            result_right = self.hasPathSum(root.right, sum - root.val)
        return result_left | result_right

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        node_count = len(postorder)
        if node_count <= 0:
            return None

        root_val = postorder[-1]
        root_inx = inorder.index(root_val)

        result = TreeNode(root_val)
        if root_inx == 0:
            result.left = None
        else:
            result.left = self.buildTree(inorder[0:root_inx], postorder[0:root_inx])
        if root_inx == node_count - 1:
            result.right = None
        else:
            result.right = self.buildTree(inorder[(root_inx + 1):], postorder[root_inx:-1])
        return result

    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        node_count = len(preorder)
        if node_count <= 0:
            return None

        root_val = preorder[0]
        root_inx = inorder.index(root_val)

        result = TreeNode(root_val)
        if root_inx == 0:
            result.left = None
        else:
            result.left = self.buildTree(preorder[1:(root_inx + 1)], inorder[:root_inx])
        if root_inx == node_count - 1:
            result.right = None
        else:
            result.right = self.buildTree(preorder[(root_inx + 1):], inorder[(root_inx + 1):])
        return result

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        def get_next_right(node_next, node_to_point):
            if not node_next:
                return
            if node_next.left:
                node_to_point.next = node_next.left
            elif node_next.right:
                node_to_point.next = node_next.right
            else:
                get_next_right(node_next.next, node_to_point)

        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                get_next_right(root.next, root.left)
        if root.right:
            get_next_right(root.next, root.right)
        self.connect(root.right)
        self.connect(root.left)
        # @connect(root.right)should be the first!!!


if __name__ == '__main__':
    t1 = [2, 0, 1, 1, 7, 0, 2, 9, 3, 8, 1, 8]
    t2 = [2, 0, 1, 0, 7, 1, 9, 8, 8, 1, 3, 2]

    tree = Solution().buildTree(t1, t2)
