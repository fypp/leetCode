class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
                results.append([v]+res)
        init = []
        for result in results:
            if result not in init:
                init.append(result)
        return init


c = Solution().permuteUnique([1,1,2])
print(c)
