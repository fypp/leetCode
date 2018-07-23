class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_origin = nums
        self.nums_now = [x for x in nums]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums_origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        import random
        random.shuffle(self.nums_now)
        return self.nums_now

    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.reset()
    # param_2 = obj.shuffle()


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


