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
        for i, v in enumerate(s):
            if count_dict[v] == 1:
                return i
        return -1

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        return s_list == t_list

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        pattern = re.compile("[a-z0-9]+")
        word_list = pattern.findall(s.lower())
        if s == "":
            return True
        str_list = list("".join(word_list))
        for i in range(len(str_list) // 2):
            if str_list[i] != str_list[-1 * (i + 1)]:
                return False
        return True

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        import re
        pattern = re.compile("^\\s*[+-]{0,1}\\d+")
        str_find = pattern.search(str)
        if str_find is None:
            return 0
        else:
            str_value = int(str_find.group(0))
            INT_MAX = 2 ** 31 - 1
            INT_MIN = -1 * 2 ** 31
            if str_value > INT_MAX:
                return INT_MAX
            if str_value < INT_MIN:
                return INT_MIN
            return int(str_value)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        int_list = list(self.countAndSay(n - 1))
        value_init = int_list[0]
        count_init = 0
        result = []
        for value in int_list:
            if value == value_init:
                count_init += 1
            else:
                result.append((count_init, value_init))
                value_init = value
                count_init = 1
        result.append((count_init, value_init))
        return_result = [str(x[0]) + str(x[1]) for x in result]
        return "".join(return_result)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for str in strs:
            while str.find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
            if prefix == "":
                return ""
        return prefix
