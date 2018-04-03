class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for inx, num in enumerate(nums):
            num_target = target - num
            if num_target in nums:
                inx_target = nums.index(num_target)
                if inx_target != inx:
                    return [inx, inx_target]
                elif num_target in nums[inx + 1:]:
                    inx_target = nums.index(num_target, inx + 1)
                    return [inx, inx_target]

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        last_value = nums[0]
        ix = 1
        for i in range(1, len(nums)):

            if nums[ix] == last_value:
                nums.pop(ix)
            else:
                last_value = nums[ix]
                ix += 1
        return ix

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_diff = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        prices_diff = [x if x > 0 else 0 for x in prices_diff]
        return sum(prices_diff)

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > 0:
            for i in range(k):
                val = nums.pop(-1)
                nums.insert(0, val)

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            else:
                num_dict[num] = 1
        return False

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict.pop(num)
            else:
                num_dict[num] = 1
        return list(num_dict.keys())[0]

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num1 in nums1:
            if num1 in nums2:
                result.append(num1)
                nums2.pop(nums2.index(num1))
        return result

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = 0
        for ix in range(len(digits)):
            value += digits[-1 - ix] * (10 ** ix)

        value += 1

        result = []
        while value > 9:
            result.append(value % 10)
            value //= 10

        result.append(value)
        result.reverse()

        return result

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ix = 0
        for i in range(len(nums)):
            if nums[ix] == 0:
                nums.pop(ix)
                ix -= 1
                nums.append(0)
            ix += 1

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            try:
                j = nums.index(target - v, i + 1)
                return [i, j]
            except ValueError:
                pass

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            row = []
            for j in range(len(board)):
                value = board[i][j]
                if value != ".":
                    row.append(value)
            if len(row) != len(set(row)):
                return False

        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                value = board[j][i]
                if value != ".":
                    col.append(value)
            if len(col) != len(set(col)):
                return False

        def check_block(board, init_ix, init_yx):
            value_block = []
            for ix in range(3):
                for jx in range(3):
                    value = board[3 * init_ix + ix][3 * init_yx + jx]
                    if value != ".":
                        value_block.append(value)
            if len(value_block) != len(set(value_block)):
                return False
            return True

        for i in range(len(board) // 3):
            for j in range(len(board) // 3):
                result = check_block(board, i, j)
                if not result:
                    return result

        return result

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        dim = len(matrix)
        for i in range(1, dim):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(dim):
                matrix[i] = matrix[i][::-1]
