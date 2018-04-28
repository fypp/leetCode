class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        len_nums = len(nums)
        result = []

        first = None
        for i in range(len_nums - 2):
            if nums[i] == first:
                continue
            first = nums[i]
            target = 0 - nums[i]
            j, k = i+1, len_nums-1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    result.append([first, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k:
                        if nums[j] != nums[j-1]:
                            break
                        if nums[k] != nums[k+1]:
                            break
                        j += 1
                        k -= 1

        return result

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0


    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagram_dict = {}
        for input_str in strs:
            key = "".join(sorted(input_str))
            if key in anagram_dict:
                anagram_dict[key].append(input_str)
            else:
                anagram_dict[key] = [input_str]
        result = [value for value in anagram_dict.values()]
        return result

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        char_list = []
        for char in s:
            if char not in char_list:
                char_list.append(char)
            else:
                ix = char_list.index(char)
                char_list = char_list[ix+1:]
                char_list.append(char)
            tmp_len = len(char_list)
            if tmp_len > max_len:
                max_len = tmp_len
        return max_len

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        max_len = 0
        max_str = ""
        if s_len <=1:
            return s
        for i in range(s_len):
            max_iter = min(i, s_len-1-i)
            for j in range(max_iter+1):
                if s[i-j] == s[i+j]:
                    palindrome_str = s[i-j:i+j+1]
                    palindrome_len = len(palindrome_str)
                    if max_len < palindrome_len:
                        max_len = palindrome_len
                        max_str = palindrome_str
                else:
                    break
        for i in range(s_len-1):
            max_iter = min(i, s_len-2-i)
            for j in range(max_iter+1):
                if s[i-j] == s[i+j+1]:
                    palindrome_str = s[i-j:i+j+2]
                    palindrome_len = len(palindrome_str)
                    if max_len < palindrome_len:
                        max_len = palindrome_len
                        max_str = palindrome_str
                else:
                    break

        return max_str



    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False
        first = None
        second = None
        for i in range(len(nums)):
            if second is not None and nums[i] > second:
                return True
            if first is None or first >= nums[i]:
                first = nums[i]
            elif nums[i] > first:
                second = nums[i]
        return False
