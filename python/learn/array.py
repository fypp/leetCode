class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        total_value = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == (total_value - nums[i]) / 2:
                return i
            left_sum += nums[i]
        return -1

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = -1
        max_ix = -1

        for i in range(len(nums)):
            if max_value < nums[i]:
                max_value = nums[i]
                max_ix = i

        for i in range(len(nums)):
            if i != max_ix and max_value < nums[i] * 2:
                return -1

        return max_ix

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        i = 0
        j = 0
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]

        n = len(matrix[0])
        if n == 0:
            return []
        if n == 1:
            return [x[0] for x in matrix]

        result = [matrix[0][0]]
        while i < m - 1 or j < n - 1:
            j += 1
            if j < n:
                result.append(matrix[i][j])
            while j > 0 and i < m - 1:
                i += 1
                j -= 1
                result.append(matrix[i][j])
            i += 1
            if i < m:
                result.append(matrix[i][j])

            while i > 0 and j < n - 1:
                i -= 1
                j += 1
                result.append(matrix[i][j])
        return result

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        try:
            return bin(int(a, 2) + int(b, 2))[2:]
        except TypeError:
            return None

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) % 2 != 0:
            return 0
        nums = sorted(nums)
        total = 0
        for i in range(len(nums) // 2):
            total += nums[i * 2]
        return total

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) == 0:
            return []

        ix = 0
        jx = len(numbers) - 1

        while ix < jx:
            if numbers[ix] + numbers[jx] < target:
                ix += 1
            elif numbers[ix] + numbers[jx] > target:
                jx -= 1
            else:
                return [ix, jx]

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        num = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num = 0
            else:
                num += 1
            if result < num:
                result = num
        return result

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        j = 0
        result = len(nums) + 1
        num_sum = nums[0]

        while i <= j < len(nums):
            if num_sum < s:
                j += 1
                if j < len(nums):
                    num_sum += nums[j]
            else:
                if j - i + 1 < result:
                    result = j - i + 1
                num_sum -= nums[i]
                i += 1
        if result == len(nums) + 1:
            return 0
        else:
            return result

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]

        row_ix = 1
        row = [1, 1]

        while row_ix < rowIndex:
            for j in range(len(row)-1):
                row[j] = row[j] + row[j+1]
            row.pop(-1)
            row.insert(0, 1)
            row.append(1)
            row_ix += 1

        return row

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        while "" in s_list:
            s_list.remove("")

        return " ".join(s_list[::-1])

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        s_reverse_list = [x[::-1] for x in s_list]
        return " ".join(s_reverse_list)