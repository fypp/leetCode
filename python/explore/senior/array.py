class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre_list = []
        back_list = []
        tmp = 1
        for num in nums:
            tmp *= num
            pre_list.append(tmp)
        pre_list.insert(0, 1)

        tmp = 1
        for num in nums[::-1]:
            tmp *= num
            back_list.append(tmp)
        back_list.insert(0, 1)
        back_list = back_list[::-1]

        result_list = []
        for i in range(len(nums)):
            result_list.append(pre_list[i] * back_list[i + 1])
        return result_list

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if len(matrix) == 0:
            return []
        i_max, j_max = len(matrix), len(matrix[0])
        tmp = []
        for j in range(j_max):
            tmp.append(matrix[0][j])
        matrix.pop(0)
        result += tmp
        if len(matrix) == 0:
            return result
        tmp = []
        for i in range(i_max - 1):
            tmp.append(matrix[i][-1])
            matrix[i].pop(-1)
        result += tmp
        if len(matrix[0]) == 0:
            return result
        tmp = []
        if len(matrix) > 0:
            for j in range(j_max - 1):
                tmp.append(matrix[-1][-1 - j])
            matrix.pop(-1)
        result += tmp
        tmp = []
        for i in range(i_max - 2):
            tmp.append(matrix[-1 - i][0])
            matrix[-1 - i].pop(0)
        result += tmp
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return result
        result += self.spiralOrder(matrix)
        return result

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        CA = Counter(A)
        CB = Counter(B)
        value_dict1 = {}
        for k, v in CA.items():
            for k2, v2 in CB.items():
                if k + k2 in value_dict1:
                    value_dict1[k + k2] += v * v2
                else:
                    value_dict1[k + k2] = v * v2

        CC = Counter(C)
        CD = Counter(D)
        value_dict2 = {}
        for k, v in CC.items():
            for k2, v2 in CD.items():
                if k + k2 in value_dict2:
                    value_dict2[k + k2] += v * v2
                else:
                    value_dict2[k + k2] = v * v2

        count = 0
        for k, v in value_dict1.items():
            if -k in value_dict2:
                count += v * value_dict2[-k]

        return count

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        final_max = 0

        while i <= j:
            area_raw = (j - i) * min(height[i], height[j])
            final_max = area_raw if final_max < area_raw else final_max
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return final_max

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        status_dict = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                node_surround = []
                for ix in [i - 1, i, i + 1]:
                    for jx in [j - 1, j, j + 1]:
                        try:
                            if ix >= 0 and jx >= 0 and not (ix == i and jx == j):
                                node_surround.append(board[ix][jx])
                        except IndexError:
                            pass

                node_count = sum(node_surround)
                node_status = board[i][j]

                if node_status == 1:
                    if node_count == 2 or node_count == 3:
                        status_dict[(i, j)] = 1
                    else:
                        status_dict[(i, j)] = 0
                else:
                    if node_count == 3:
                        status_dict[(i, j)] = 1
                    else:
                        status_dict[(i, j)] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = status_dict[(i, j)]

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1

        k = 0
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] <= len(nums):
                nums[k] = nums[i]
                k += 1

        for i in range(k):
            val = abs(nums[i])
            nums[val - 1] = -abs(nums[val - 1])

        for i in range(k):
            if nums[i] > 0:
                return i + 1

        return k + 1

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        len_dict = {}
        for num in nums:
            if num in len_dict:
                continue
            seq_list = [num]
            last = num - 1
            while last in nums:
                seq_list.append(last)
                last -= 1
            next = num + 1
            while next in nums:
                seq_list.append(next)
                next += 1
            for v in seq_list:
                len_dict[v] = len(seq_list)
        return max(len_dict.values())

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, t = 0, 0, 0
        while (True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break;

        while (True):
            slow = nums[slow]
            t = nums[t]
            if (slow == t):
                break

        return slow

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        import re
        digits = re.findall("\\d+", s)
        if len(digits) == 1:
            return int(digits[0])
        operators = re.findall("[\+\-\*\/]", s)
        first_calculate = {
            "*": lambda x, y: int(x) * int(y),
            "/": lambda x, y: int(x) // int(y)
        }
        second_calculate = {
            "+": lambda x, y: int(x) + int(y),
            "-": lambda x, y: int(x) - int(y),
        }
        while len(operators) > 1:
            if operators[0] in first_calculate:
                digits[1] = first_calculate[operators[0]](digits[0], digits[1])
                digits.pop(0)
                operators.pop(0)
            elif operators[1] in first_calculate:
                digits[2] = first_calculate[operators[1]](digits[1], digits[2])
                digits.pop(1)
                operators.pop(1)
            else:
                digits[1] = second_calculate[operators[0]](digits[0], digits[1])
                digits.pop(0)
                operators.pop(0)
        if operators[0] in first_calculate:
            return first_calculate[operators[0]](digits[0], digits[1])
        else:
            return second_calculate[operators[0]](digits[0], digits[1])

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        i = k - 1
        window = nums[:i]
        result = []
        while i < len(nums):
            window.append(nums[i])
            result.append(max(window))
            window.pop(0)
            i += 1
        return result

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = ""

        i, j = 0, 0
        min_length = len(s)
        from collections import Counter
        t_counter = Counter(t)

        while i < len(s):
            if max(t_counter.values()) > 0:
                if j < len(s) and s[j] in t_counter:
                    t_counter[s[j]] -= 1
                if j == len(s):
                    break
                j += 1
            else:
                if min_length >= j - i:
                    min_length = j - i
                    result = s[i:j]
                if s[i] in t_counter:
                    t_counter[s[i]] += 1
                i += 1

        return result


print(Solution().minWindow("ABC", "AC"))
