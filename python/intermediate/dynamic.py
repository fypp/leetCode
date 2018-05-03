class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        meet_ix = len(nums)
        for i in range(1, len(nums)):
            if len(nums) - i + nums[len(nums) - 1 - i] >= meet_ix:
                meet_ix = len(nums) - i
        if meet_ix == 1:
            return True
        return False

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        value1 = 1
        for i in range(1, m + n - 1):
            value1 *= i
        value21 = 1
        for j in range(1, n):
            value21 *= j
        value22 = 1
        for j in range(1, m):
            value22 *= j
        return value1 / (value21 * value22)

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1

        if len(coins) == 1:
            if amount == coins[0]:
                return 1

        change_dict = {0: 0}
        for i in range(1, amount + 1):
            change_dict[i] = float("inf")
            for j in range(len(coins)):
                if i >= coins[j]:
                    change_dict[i] = min(change_dict[i], change_dict[i - coins[j]] + 1)
        if change_dict[amount] > amount:
            return -1
        else:
            return change_dict[amount]

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        num_seq = [nums[0]]
        for i in range(1, len(nums)):
            if num_seq[0] >= nums[i]:
                num_seq[0] = nums[i]
                continue
            for j in range(len(num_seq)):
                if j + 1 < len(num_seq):
                    if num_seq[j] < nums[i] <= num_seq[j + 1]:
                        num_seq[j+1] = nums[i]
                        break
                else:
                    num_seq.append(nums[i])
        return len(num_seq)


t = Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
print(t)
