class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 2

        if n == 1:
            return first
        if n == 2:
            return second

        for i in range(2, n):
            next = first + second
            first = second
            second = next

        return next

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        total = max(nums)
        if len(nums) == 1:
            return nums[0]
        if total < 0:
            return total
        else:
            total = 0
        max_array = total

        for num in nums:
            total += num
            if total <= 0:
                total = 0
            if total > max_array:
                max_array = total
        return max_array

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        try:
            first_grow = [1 if x > 0 else 0 for x in prices_diff].index(1)
        except:
            return 0
        return self.maxSubArray(prices_diff[first_grow:])

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        ix_median = len(nums) // 2 - 1

        return max(self.rob(nums[:ix_median]) + self.rob(nums[ix_median + 1:]),
                   self.rob(nums[:ix_median+1]) + self.rob(nums[ix_median+2:]),
                   self.rob(nums[:ix_median-1]) + self.rob(nums[ix_median:]))
