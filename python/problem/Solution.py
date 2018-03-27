
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
                elif num_target in nums[inx+1:]:
                    inx_target = nums.index(num_target, inx+1)
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
        for i in range(1,len(nums)):

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
        prices_diff = [prices[i + 1]-prices[i] for i in range(len(prices)-1)]
        prices_diff = [x if x>0 else 0 for x in prices_diff]
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
