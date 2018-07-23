class Solution(object):
    def combination(self, str_list):
        result = []
        if len(str_list) == 0:
            return []
        if len(str_list) == 1:
            return [x for x in str_list[0]]
        for x in str_list[0]:
            next_str = Solution().combination(str_list[1:])
            for n in next_str:
                result.append(x + n)
        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        com = {"2": "abc", "3": "def", "4": "ghi",
               "5": "jkl", "6": "mno", "7": "pqrs",
               "8": "tuv", "9": "wxyz"}
        input_list = []
        for digit in digits:
            input_list.append(com[digit])

        return Solution().combination(input_list)

    def generateQuotes(self, quote_list):
        result = []
        if len(quote_list) == 0:
            return []
        elif len(quote_list) == 1:
            return quote_list[0]
        result_next = Solution().generateQuotes(quote_list[1:])
        for v in result_next:
            for i in range(len(v) + 1):
                tmp = list(v).copy()
                tmp.insert(i, quote_list[0])
                result.append("".join(tmp))
        return list(set(result))

    def checkQuotes(self, quote):
        quote_list = list(quote)
        if quote_list == []:
            return True
        if quote_list[0] != "(":
            return False
        quote_next = quote_list[1:]
        ix = quote_next.index(")")
        quote_next.pop(ix)
        return Solution().checkQuotes(quote_next)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        char_list = ["("] * n + [")"] * n
        qotes = Solution().generateQuotes(char_list)
        result = []
        for char in qotes:
            if Solution().checkQuotes(char):
                result.append(char)
        return result

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        result_next = Solution().permute(nums[1:])
        for x in result_next:
            for i in range(len(x) + 1):
                tmp = x[:]
                tmp.insert(i, nums[0])
                result.append(tmp)
        return result

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums, []]
        result = [[]]
        for i in range(len(nums)):
            for j in range(len(result)):
                result.append(result[j][:])
                result[j].append(nums[i])
        return result

    def nearPoint(self, i, j, board, check, expl):
        if i >= 0 and i < len(board) and j >= 0 and j < len(board[i]):
            word = board[i][j]
        else:
            return False

        if len(check) == 1:
            if word == check[0]:
                return True
            else:
                return False
        if check[0] != word:
            return False

        explore = expl.copy()
        explore[(i, j)] = 1
        next_word = check[1:]
        if i - 1 >= 0 and (i - 1, j) not in explore:
            result = Solution().nearPoint(i - 1, j, board, next_word, explore)
            if result:
                return True
        if j - 1 >= 0 and (i, j - 1) not in explore:
            result = Solution().nearPoint(i, j - 1, board, next_word, explore)
            if result:
                return True
        if i + 1 < len(board) and (i + 1, j) not in explore:
            result = Solution().nearPoint(i + 1, j, board, next_word, explore)
            if result:
                return True
        if j + 1 < len(board[i]) and (i, j + 1) not in explore:
            result = Solution().nearPoint(i, j + 1, board, next_word, explore)
            if result:
                return True
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        word_dict = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                w = board[i][j]
                if w in word_dict:
                    word_dict[w].append((i, j))
                else:
                    word_dict[w] = [(i, j)]
        if word[0] not in word_dict:
            return False
        for (i, j) in word_dict[word[0]]:
            result = Solution().nearPoint(i, j, board, list(word), {})
            if result:
                return True
        return False


t = Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
print(t)
