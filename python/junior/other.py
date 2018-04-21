class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n)
        return list(bin_n[2:]).count("1")

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = list(bin(x)[2:])
        bin_y = list(bin(y)[2:])
        while len(bin_y) < len(bin_x):
            bin_y.insert(0, "0")
        while len(bin_x) < len(bin_y):
            bin_x.insert(0, "0")
        result = [1 if bin_x[i] != bin_y[i] else 0 for i in range(len(bin_x))]
        return result.count(1)

    def reverseBits(self, n):
        bin_n = list(bin(n)[2:])
        while len(bin_n) != 32:
            bin_n.insert(0, "0")
        result = "".join(bin_n[::-1])
        return int(result, 2)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return []
        result.append([1])
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result

        row_before = [1, 1]
        for i in range(2, numRows):
            row = [1, 1]
            for j in range(1, len(row_before)):
                row.insert(j, row_before[j - 1] + row_before[j])
            result.append(row)
            row_before = row
        return result

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        if s_len == 0:
            return True
        if s_len % 2 != 0:
            return False

        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        s_list = list(s)
        try:
            max_ix = -1
            left_ix = -1
            for i in range(len(left)):
                try:
                    ix = len(s_list) - 1 - s_list[::-1].index(left[i])
                    if ix > max_ix:
                        max_ix = ix
                        left_ix = i
                except ValueError:
                    pass
            sx = s_list.index(right[left_ix], max_ix)

            result_other = self.isValid("".join(s_list[:max_ix]+s_list[sx+1:]))
            result_middle = self.isValid("".join(s_list[max_ix + 1:sx]))
            if result_middle and result_other:
                return True
            else:
                return False

        except ValueError:
            return False

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_dict = {}
        for num in nums:
            nums_dict[num] = 1

        for i in range(len(nums)+1):
            if i not in nums_dict:
                return i
