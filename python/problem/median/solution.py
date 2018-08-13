class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # ZigZag Conversion
    def get_poped_result(self, result, s_list, sep):
        ix_init = list(range(0, len(s_list), sep))
        pop_ix = [0]
        for v in ix_init[1:]:
            pop_ix.append(v - 1)
            pop_ix.append(v)
        if sep + pop_ix[-1] == len(s_list):
            pop_ix.append(len(s_list) - 1)
        for i, v in enumerate(pop_ix):
            result.append(s_list.pop(v - i))
        return result

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows:
            return s
        if numRows == 1:
            return s

        s_list = list(s)
        result = []
        sep = 2 * (numRows - 1)

        # 第0层数据
        ix_init = range(0, len(s_list), sep)
        for i, v in enumerate(ix_init):
            result.append(s_list.pop(v - i))

        # 第一层数据
        if sep == 2:
            result += s_list
        else:
            sep = sep - 1
            result = self.get_poped_result(result, s_list, sep)

        # 第二层及以上
        sep -= 2
        while sep > 1:
            result = self.get_poped_result(result, s_list, sep)
            sep -= 2
        if sep == 1:
            result += s_list
        return "".join(result)

    #  Integer to Roman
    def intToRomanBasic(self, num_dict, num):
        if num < 4:
            return num_dict[1] * num
        elif num == 4:
            return num_dict[1] + num_dict[5]
        elif num == 5:
            return num_dict[5]
        elif num < 9:
            return num_dict[5] + num_dict[1] * (num - 5)
        elif num == 9:
            return num_dict[1] + num_dict[10]
        else:
            return num_dict[10]

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_dict1 = {1: "I", 5: "V", 10: "X"}
        num_dict2 = {1: "X", 5: "L", 10: "C"}
        num_dict3 = {1: "C", 5: "D", 10: "M"}
        if num <= 10:
            return self.intToRomanBasic(num_dict1, num)
        elif num <= 100:
            num1 = num // 10
            num2 = num - 10 * num1
            return self.intToRomanBasic(num_dict2, num1) + self.intToRomanBasic(num_dict1, num2)
        elif num <= 1000:
            num1 = num // 100
            num2 = (num - 100 * num1) // 10
            num3 = num - 100 * num1 - 10 * num2
            return self.intToRomanBasic(num_dict3, num1) + self.intToRomanBasic(num_dict2, num2) + self.intToRomanBasic(
                num_dict1, num3)
        else:
            num0 = num // 1000
            num1 = (num - num0 * 1000) // 100
            num2 = (num - num0 * 1000 - 100 * num1) // 10
            num3 = num - num0 * 1000 - 100 * num1 - 10 * num2
            return "M" * num0 + self.intToRomanBasic(num_dict3, num1) + self.intToRomanBasic(num_dict2,
                                                                                             num2) + self.intToRomanBasic(
                num_dict1, num3)

    # 3Sum Closest
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        if len(nums) == 3:
            return sum(nums)
        result = sum(nums[:3])
        min_diff = abs(sum(nums[:3]) - target)
        nums_sorted = sorted(nums)
        for i in range(len(nums) - 2):
            ix = i + 1
            jx = len(nums) - 1
            target_two = target - nums_sorted[i]
            while jx - ix >= 1:
                sum_two = nums_sorted[ix] + nums_sorted[jx]
                if sum_two == target_two:
                    return target
                elif sum_two > target_two:
                    jx -= 1
                else:
                    ix += 1
                diff = abs(target_two - sum_two)
                if diff < min_diff:
                    min_diff = diff
                    result = sum_two - target_two + target
        return result

    def fourSum(self, num, target):
        solution = []
        num.sort()
        dict = {}
        if len(num) < 4:
            return solution
        for i in range(len(num)):
            # if i>0 and num[i]==num[i+1]:
            #   continue
            for j in range(i + 1, len(num)):
                val = num[i] + num[j]
                if val not in dict:
                    dict[val] = [[i, j]]
                else:
                    dict[val].append([i, j])
        for i in range(len(num)):
            # if i>0 and num[i]==num[i+1]:## we should delete this here
            #    continue
            for j in range(i + 1, len(num) - 2):
                dif = target - num[i] - num[j]
                if dif in dict:
                    for k in dict[dif]:
                        if k[0] > j and [num[i], num[j], num[k[0]], num[k[1]]] not in solution:
                            solution.append([num[i], num[j], num[k[0]], num[k[1]]])
        return solution

    def swapNode(self, head):
        if head.next:
            node = head.next
            tmp = head.next.next
            node.next = head
            head.next = tmp
            return node
        else:
            return head

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            head = self.swapNode(head)
            if head.next:
                node = head.next
                while node and node.next:
                    node.next = self.swapNode(node.next)
                    if node.next:
                        node = node.next.next
                    else:
                        node = node.next
            else:
                return head
            return head
        else:
            return None

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        lens = len(nums)
        for i in range(1, lens):
            if nums[-i] > nums[-i - 1]:
                for k in range(1, i + 1):
                    if nums[-k] > nums[-i - 1]:
                        tmp = nums[-i - 1]
                        nums[-i - 1] = nums[-k]
                        nums[-k] = tmp
                        break
                for j in range(lens - i, lens - i + i // 2):
                    ix2 = lens - 1 - j + lens - i
                    tmp2 = nums[ix2]
                    nums[ix2] = nums[j]
                    nums[j] = tmp2
                return
        for i in range(1, len(nums) // 2 + 1):
            tmp = nums[-i]
            nums[-i] = nums[i - 1]
            nums[i - 1] = tmp

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return None

        # 在问题足够简单情况下返回的结果
        if target == 0:
            return [[]]
        if target < 0:
            return None

        candidates = sorted(candidates)
        results = []
        # 按不同候选数， 拆分任务
        for i, candidate in enumerate(candidates):
            result_next = self.combinationSum(candidates[i:], target - candidate)
            if result_next is not None:
                for result in result_next:
                    results.append([candidate] + result)

        return results

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return None

        # 在问题足够简单情况下返回的结果
        if target == 0:
            return [[]]
        if target < 0:
            return None

        candidates = sorted(candidates)
        results = []
        # 按不同候选数， 拆分任务
        for i, candidate in enumerate(candidates):
            if i == len(candidates) - 1:
                if candidates[-1] == target:
                    results.append([candidate])
            else:
                result_next = self.combinationSum2(candidates[i + 1:], target - candidate)
                if result_next is not None:
                    for result in result_next:
                        results.append([candidate] + result)
        init = []
        for result in results:
            if result not in init:
                init.append(result)
        return init

    def transfer_str_int(self, num1):
        if num1 == "0":
            return 0
        if num1 == "1":
            return 1
        if num1 == "2":
            return 2
        if num1 == "3":
            return 3
        if num1 == "4":
            return 4
        if num1 == "5":
            return 5
        if num1 == "6":
            return 6
        if num1 == "7":
            return 7
        if num1 == "8":
            return 8
        if num1 == "9":
            return 9

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        int1 = 0
        for num in num1:
            int1 = 10 * int1 + self.transfer_str_int(num)
        int2 = 0
        for num in num2:
            int2 = 10 * int2 + self.transfer_str_int(num)
        result = int1 * int2
        return str(result)

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        if len(nums) == 0:
            return [[]]

        for v in nums:
            tmp = nums.copy()
            tmp.remove(v)
            result_next = self.permuteUnique(tmp)
            for res in result_next:
                results.append([v] + res)
        init = []
        for result in results:
            if result not in init:
                init.append(result)
        return init

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return [[]]

        init = []
        for i in range(n):
            init.append([1] * n)
        ix0 = 0
        ix1 = n - 1
        jx0 = 0
        jx1 = n - 1
        i, j, v = 0, 0, 1
        while ix0 < ix1 and jx0 < jx1:
            if i == ix0 and j < jx1:
                init[i][j] = v
                j += 1
                v += 1
            if j == jx1 and i < ix1:
                init[i][j] = v
                i += 1
                v += 1
            if i == ix1 and j > jx0:
                init[i][j] = v
                j -= 1
                v += 1
            if j == jx0 and i > ix0:
                init[i][j] = v
                i -= 1
                v += 1
            if i == ix0 and j == jx0:
                ix0 += 1
                jx0 += 1
                ix1 -= 1
                jx1 -= 1
                i = ix0
                j = jx0
        if ix0 == jx1:
            init[i][j] = v

        return init

    def get_value(self, n_list, k):
        n = len(n_list)
        if n == 1:
            return n_list
        n_list = sorted(n_list)

        import math
        num_next = math.factorial(n - 1)
        value_index = k // num_next
        k_next = k % num_next
        if k_next == 0:
            value_index -= 1
            k_next = num_next

        value = n_list[value_index]
        result = [value]
        n_list.remove(value)
        result += self.get_value(n_list, k_next)
        return result

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        n_list = list(range(1, n + 1))
        result = self.get_value(n_list, k)
        result = [str(x) for x in result]
        return "".join(result)

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        count = 1
        node = head
        while node.next:
            count += 1
            node = node.next

        for i in range(k % count):
            node = head.next
            node1 = head
            while node.next:
                node1 = node
                node = node.next
            node1.next = None
            node.next = head
            head = node

        return head

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0

        # 将原有矩阵做转置
        obstacleGrid2 = []
        for j in range(len(obstacleGrid[0])):
            row = []
            for i in range(len(obstacleGrid)):
                row.append(obstacleGrid[-i - 1][-j - 1])
            obstacleGrid2.append(row)

        obstacleGrid = obstacleGrid2
        nums_row = len(obstacleGrid)
        nums_col = len(obstacleGrid[0])

        # 计算个点对应的可能个数
        i = j = 0

        while i < nums_row and j < nums_col:
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            elif i == 0:
                if j == 0:
                    obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
            elif j == 0:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j]
            else:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

            j2 = j + 1
            while j2 < nums_col:
                if obstacleGrid[i][j2] == 1:
                    obstacleGrid[i][j2] = 0
                elif i == 0:
                    obstacleGrid[i][j2] = obstacleGrid[i][j2 - 1]
                else:
                    obstacleGrid[i][j2] = obstacleGrid[i][j2 - 1] + obstacleGrid[i - 1][j2]
                j2 += 1
            i2 = i + 1
            while i2 < nums_row:
                if obstacleGrid[i2][j] == 1:
                    obstacleGrid[i2][j] = 0
                elif j == 0:
                    obstacleGrid[i2][j] = obstacleGrid[i2 - 1][j]
                else:
                    obstacleGrid[i2][j] = obstacleGrid[i2][j - 1] + obstacleGrid[i2 - 1][j]
                i2 += 1
            i += 1
            j += 1
        return obstacleGrid[-1][-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        # 将原有矩阵做转置
        obstacleGrid = []
        for j in range(len(grid[0])):
            row = []
            for i in range(len(grid)):
                row.append(grid[-i - 1][-j - 1])
            obstacleGrid.append(row)

        nums_row = len(obstacleGrid)
        nums_col = len(obstacleGrid[0])

        i = j = 0

        while i < nums_row and j < nums_col:
            if i == 0:
                if j > 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1]
            elif j == 0:
                obstacleGrid[i][j] += obstacleGrid[i - 1][j]
            else:
                obstacleGrid[i][j] += min(obstacleGrid[i - 1][j], obstacleGrid[i][j - 1])

            j2 = j + 1
            while j2 < nums_col:
                if i == 0:
                    obstacleGrid[i][j2] += obstacleGrid[i][j2 - 1]
                else:
                    obstacleGrid[i][j2] += min(obstacleGrid[i][j2 - 1], obstacleGrid[i - 1][j2])
                j2 += 1
            i2 = i + 1
            while i2 < nums_row:
                if j == 0:
                    obstacleGrid[i2][j] += obstacleGrid[i2 - 1][j]
                else:
                    obstacleGrid[i2][j] += min(obstacleGrid[i2][j - 1], obstacleGrid[i2 - 1][j])
                i2 += 1
            i += 1
            j += 1
        return obstacleGrid[-1][-1]

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s_list = path.split("/")
        while "" in s_list:
            s_list.remove("")
        while "." in s_list:
            s_list.remove(".")
        while ".." in s_list:
            ix = s_list.index("..")
            s_list.remove("..")
            if len(s_list) == 0:
                return "/"
            if ix > 0:
                s_list.pop(ix - 1)
        return "/" + "/".join(s_list)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        #  最简单情况返回结果
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        if len(matrix[0]) == 1:
            tmp = [x[0] for x in matrix]
            if target in tmp:
                return True
            else:
                return False

        # 若列少于行则转置

        if len(matrix) > len(matrix[0]):
            obstacleGrid = []
            for j in range(len(matrix[0])):
                row = []
                for i in range(len(matrix)):
                    row.append(matrix[i][j])
                obstacleGrid.append(row)
            matrix = obstacleGrid

        ix = 0
        if matrix[0][0] == target:
            return True
        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False

        # 选择拆分矩阵的位置
        num_min = min(len(matrix), len(matrix[0]))
        for i in range(1, num_min):
            if matrix[i][i] < target:
                ix = i
            elif matrix[i][i] == target:
                return True
            else:
                break
        matrix1 = []
        for i in range(ix + 1):
            matrix1.append(matrix[i][ix + 1:])

        matrix2 = []
        for i in range(ix + 1, len(matrix)):
            matrix2.append(matrix[i][:ix + 1])

        res1 = self.searchMatrix(matrix1, target)
        res2 = self.searchMatrix(matrix2, target)

        if res1 or res2:
            return True
        else:
            return False

    def combine_list(self, n_list, k):
        result = []
        if len(n_list) < k or len(n_list) == 0:
            return [[]]
        if k == 1:
            return [[x] for x in n_list]
        n_list = sorted(n_list)
        for i in range(len(n_list) - k + 1):
            result_next = self.combine_list(n_list[i + 1:], k - 1)
            for res in result_next:
                result.append([n_list[i]] + res)
        return result

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        init = list(range(1, n + 1))
        result = self.combine_list(init, k)
        return result

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        value = nums[-1]
        count = 1
        for i in range(len(nums) - 2, -1, -1):
            if value == nums[i]:
                count += 1
                if count > 2:
                    nums.pop(i)
            else:
                value = nums[i]
                count = 1
        return len(nums)

    def find_rotate_point(self, nums):
        i = 0
        j = len(nums) - 1
        middle = (i + j) // 2
        if j - i <= 1:
            return i

        if nums[i] > nums[middle]:
            return self.find_rotate_point(nums[i:middle + 1])
        elif nums[i] < nums[middle]:
            return middle + self.find_rotate_point(nums[middle:])
        else:
            return 1 + self.find_rotate_point(nums[1:])

    def find_point(self, nums, target):

        if nums[0] > target or nums[-1] < target:
            return False

        i = 0
        j = len(nums) - 1
        middle = (i + j) // 2
        if i == j:
            if nums[0] == target:
                return True
            else:
                return False
        if nums[middle] < target:
            return self.find_point(nums[middle + 1:], target)
        elif nums[middle] == target:
            return True
        else:
            return self.find_point(nums[:middle], target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if target in nums:
                return True
            else:
                return False

        # 找到旋转点
        ix = self.find_rotate_point(nums)

        #  分别对有序数组二分查找
        res1 = self.find_point(nums[:ix + 1], target)
        res2 = self.find_point(nums[ix + 1:], target)
        if res1 or res2:
            return True
        else:
            return False

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        node_last = None
        node = head
        tmp = head.val

        if head.next and head.next.val == tmp:
            node2 = head.next
            while node2 and node2.val == tmp:
                node2 = node2.next
            return self.deleteDuplicates(node2)

        while node and node.next:
            node_next = node.next
            is_duplicate = False
            while node_next and node_next.val == tmp:
                node_next = node_next.next
                is_duplicate = True
            if is_duplicate:
                node_last.next = node_next
            else:
                node_last = node
            if node_next:
                tmp = node_next.val
                node = node_next
            else:
                node = None

        return head

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node = head
        res1 = []
        res2 = []
        while node:
            if node.val < x:
                res1.append(node)
            else:
                res2.append(node)
            node = node.next
        res = (res1 + res2)[::-1]
        if len(res) == 0:
            return None
        if len(res) == 1:
            return res[0]
        res[0].next = None
        for i in range(1, len(res)):
            res[i].next = res[i - 1]
        return res[-1]

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return []

        init = ["0", "1"]
        if n == 1:
            return init

        count = 1
        while count < n:
            res = []
            for v in init:
                res.append("0" + v)
            for v in init[::-1]:
                res.append("1" + v)
            init = res
            count += 1

        result = [int(x, 2) for x in init]
        return result

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[], nums]

        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            res_next = self.subsetsWithDup(nums[i + 1:])
            for re in res_next:
                res.append([nums[i]] + re)

        result = [[]]
        for re in res:
            if re not in result:
                result.append(re)

        return result

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0 or s[0] == "0":
            return 0

        if len(s) == 1:
            return 1

        ways = [0, 1]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                ways.append(0)
            elif len(s[i:i + 2]) == 0 or int(s[i:i + 2]) <= 26:
                count = ways[-2] + ways[-1]
                ways.append(count)
            else:
                ways.append(ways[-1])
        return ways[-1]

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        node = head
        node12 = head
        node22 = head
        index = 1

        while index < m:
            node12 = node
            node22 = node.next
            node = node22
            index += 1

        if node22.next:
            node21 = node22.next
        else:
            node21 = node22
        node31 = node21.next
        if m == n:
            node21 = node22
            node = node21
        else:
            node = node22
            while index < n:
                node22.next = node31
                node21.next = node
                node = node21
                node21 = node31
                if node31:
                    node31 = node31.next
                index += 1

        if m == 1:
            return node
        else:
            node12.next = node
            return head

    def isIpAddress(self, s, n):
        if len(s) == 0:
            return [None]
        if n == 1:
            if s[0] == "0":
                if s == "0":
                    return [[s]]
                else:
                    return [None]
            else:
                if int(s) <= 255:
                    return [[s]]
                else:
                    return [None]

        result = []
        s_list = list(s)
        for i in range(min(len(s), 3)):
            if s_list[0] == "0" and i > 0:
                continue
            if int("".join(s_list[:i + 1])) > 255:
                continue
            res_list = self.isIpAddress("".join(s_list[i + 1:]), n - 1)
            for res in res_list:
                if res:
                    result.append(["".join(s_list[:i + 1])] + res)
        return result

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        res = self.isIpAddress(s, 4)
        result = [".".join(x) for x in res]
        return result

    def generateTreeList(self, nums):

        if len(nums) == 0:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        result = []
        for i in range(len(nums)):
            trees_left = self.generateTreeList(nums[:i])
            trees_right = self.generateTreeList(nums[i + 1:])
            for tree_left in trees_left:
                for tree_right in trees_right:
                    tree = TreeNode(nums[i])
                    tree.left = tree_left
                    tree.right = tree_right
                    result.append(tree)
        return result

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        nums = list(range(1, n + 1))
        return self.generateTreeList(nums)

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        if n <= 1:
            return res[n]

        for i in range(2, n + 1):
            tmp = 0
            for j in range(i):
                tmp += res[j] * res[i - 1 - j]
            res.append(tmp)
        return res[-1]

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if head is None:
            return None

        # 计算链表对应子节点个数
        node = head
        num = 1
        while node.next:
            num += 1
            node = node.next

        # 子问题对应解决方案
        if num == 1:
            return TreeNode(node.val)
        if num == 2:
            node_left = TreeNode(head.val)
            node_root = TreeNode(node.val)
            node_root.left = node_left
            return node_root

        # 链表分拆递归求解
        middle = num // 2
        count = 1
        node = head
        node_parent = None
        while count <= middle:
            node_parent = node
            node = node.next
            count += 1

        node_parent.next = None
        list_left = head
        list_right = node.next
        node_root = TreeNode(node.val)
        node_root.left = self.sortedListToBST(list_left)
        node_root.right = self.sortedListToBST(list_right)

        return node_root

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        if root.left is None and root.right is None:
            if root.val == sum:
                return [[sum]]
            else:
                return []

        result = []
        root_val = root.val
        if root.left:
            results_left = self.pathSum(root.left, sum - root_val)
            for res in results_left:
                result.append([root_val] + res)
        if root.right:
            results_right = self.pathSum(root.right, sum - root_val)
            for res in results_right:
                result.append([root_val] + res)
        return result

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                node.right = root.right
                root.right = root.left
                root.left = None

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(2, len(triangle) + 1):
            tmp = triangle[-i]
            for j in range(len(tmp)):
                tmp[j] += min(triangle[-i + 1][j], triangle[-i + 1][j + 1])
        return triangle[0][0]

    def canTransformList(self, word):
        result = {word}
        for i in range(len(word)):
            for cx in range(ord("a"), ord("z") + 1):
                result.add(word[:i] + chr(cx) + word[i + 1:])
        result.remove(word)
        return result

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        word_dict = {endWord}
        for x in wordList:
            word_dict.add(x)
        level = 1
        words = [endWord]
        while len(words) > 0:
            transform_list = []
            for word in words:
                transform_list += self.canTransformList(word)
            words = []
            level += 1
            for trans in transform_list:
                if trans == beginWord:
                    return level
                if trans in word_dict:
                    words.append(trans)
        return 0



c = Solution().minSubArrayLen(4,[1,4,4])
print(c)
