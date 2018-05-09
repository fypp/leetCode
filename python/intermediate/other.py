class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        site_diff = a ^ b
        site_and = a & b

        while site_and != 0:
            site_next = site_and << 1
            site_and = (site_diff & site_next) % 0x100000000
            site_diff = (site_diff ^ site_next) % 0x100000000
        return site_diff if site_diff <= 0x7FFFFFFF else site_diff | (~0x100000000 + 1)

    def process(self, a, b, c):
        if c == "+":
            return str(int(a) + int(b))
        if c == "-":
            return str(int(a) - int(b))
        if c == "*":
            return str(int(a) * int(b))
        if c == "/":
            if int(a) * int(b) < 0 and int(a) % int(b) != 0:
                return str(int(a) // int(b) + 1)
            return str(int(a) // int(b))

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) == 3:
            return int(self.process(tokens[0], tokens[1], tokens[2]))
        operators = ["+", "-", "*", "/"]
        result = []
        for i, v in enumerate(tokens):
            if v in operators:
                ans = int(self.process(result[-2], result[-1], v))
                result.pop(-1)
                result.pop(-1)
                result.append(ans)
            else:
                result.append(v)
        return result[0]

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        threshold = len(nums) // 2
        appear_times = {}

        for num in nums:
            if num in appear_times:
                appear_times[num] += 1
                if appear_times[num] > threshold:
                    return num
            else:
                appear_times[num] = 1

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        from collections import Counter
        counter = Counter(tasks)
        counter_list = sorted([(i, v) for i, v in counter.items()], key=lambda x: x[1], reverse=True)
        tasks_processed = [""] * (n + 1) * counter_list[0][1]
        ix = 0
        for i in range(len(counter_list)):
            while tasks_processed[ix] != "":
                ix += 1
                if ix >= len(tasks_processed):
                    return len(tasks)
            for j in range(counter_list[i][1]):
                if j * (n + 1) + ix >= len(tasks_processed):
                    return len(tasks)
                tasks_processed[j * (n + 1) + ix] = counter_list[i][0]
        result = len(tasks_processed)
        for i in range(n + 1):
            if tasks_processed[-1 - i] == "":
                result -= 1
            else:
                return result


