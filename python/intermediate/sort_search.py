class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_dict = {0: 0, 1: 0, 2: 0}
        for num in nums:
            num_dict[num] += 1
        nums[:num_dict[0]] = [0] * num_dict[0]
        nums[num_dict[0]:num_dict[0] + num_dict[1]] = [1] * num_dict[1]
        nums[num_dict[1] + num_dict[0]:num_dict[0] + num_dict[1] + num_dict[2]] = [2] * num_dict[2]

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = {}
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        count_k = sorted(nums_count.values(), reverse=True)[k - 1]
        result = []
        for num in nums_count:
            if nums_count[num] >= count_k:
                result.append(num)
        return result

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        nums.insert(0, float("-inf"))
        nums.insert(len(nums), float("-inf"))
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i + 1
        return None

    def findFirst(self, nums, target):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return None
        if len(nums) == 2:
            if nums[0] == target:
                return 1
            if nums[1] == target:
                return 2
            else:
                return None
        ix = len(nums) // 2
        left = Solution().findFirst(nums[:ix], target)
        right = Solution().findFirst(nums[ix:], target)
        if left:
            return left
        elif right:
            var = ix + right
            return var
        else:
            return None

    def findLast(self, nums, target):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return None
        if len(nums) == 2:
            if nums[1] == target:
                return 2
            if nums[0] == target:
                return 1
            else:
                return None
        ix = len(nums) // 2
        left = Solution().findLast(nums[:ix], target)
        right = Solution().findLast(nums[ix:], target)
        if right:
            var = ix + right
            return var
        elif left:
            return left
        else:
            return None

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = Solution().findFirst(nums, target)
        right = Solution().findLast(nums, target)
        if left:
            return [left - 1, right - 1]
        else:
            return [-1, -1]

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        result = [intervals[0]]
        for interval in intervals[1:]:
            last = result[-1]
            if last.end >= interval.start:
                if last.end < interval.end:
                    last.end = interval.end
            else:
                result.append(interval)
        return result

    def searchIx(self, nums, target):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return None
        ix = len(nums) // 2
        left = Solution().searchIx(nums[:ix], target)
        right = Solution().searchIx(nums[ix:], target)
        if left:
            return left
        elif right:
            return ix + right
        else:
            return None

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        ix = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                ix = i
        ix1 = Solution().searchIx(nums[:ix], target)
        if ix1:
            return ix1 - 1
        ix2 = Solution().searchIx(nums[ix:], target)
        if ix2:
            return ix + ix2 - 1
        return -1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        j = len(matrix[0]) - 1
        i = 0
        while i < len(matrix) and j>=0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False


