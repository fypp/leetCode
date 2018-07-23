# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes = [[root]]
        node_child = [root]

        while node_child:
            node_next = []
            for node in node_child:
                if node.left:
                    node_next.append(node.left)
                if node.right:
                    node_next.append(node.right)
            nodes.append(node_next)
            node_child = node_next
        result = []
        for i in range(len(nodes)):
            if i % 2 == 1:
                nodes[i].reverse()
            result.append([x.val for x in nodes[i]])
        return result[:-1]

    def preTravel(self, root):
        result = []
        if not root:
            return result
        if root.left:
            result += Solution().preTravel(root.left)
        result.append(root.val)
        if root.right:
            result += Solution().preTravel(root.right)
        return result

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result = Solution().preTravel(root)
        if len(result) < k:
            return []
        else:
            return result[k - 1]

    def change(self, grid, i, j):
        grid[i][j] = 0
        if i - 1 >= 0 and grid[i-1][j] == "1":
            Solution().change(grid, i - 1, j)
        if i + 1 < len(grid) and grid[i+1][j] == "1":
            Solution().change(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j-1] == "1":
            Solution().change(grid, i, j - 1)
        if j + 1 < len(grid[0]) and grid[i][j+1] == "1":
            Solution().change(grid, i, j + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    Solution().change(grid, i, j)
                    count += 1
        return count