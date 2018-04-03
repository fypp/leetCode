class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = str(x)[::-1]
        if x < 0:
            result = -1 * int(result[:-1])
        else:
            result = int(result)
        if result < -1 * 2 ** 31 or result > 2 ** 31:
            return 0
        return result

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        count_dict = collections.Counter(s)
        for i,v in enumerate(s):
            if count_dict[v] == 1:
                return i
        return -1

