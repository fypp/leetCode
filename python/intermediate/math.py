class Solution(object):
    def transformNum(self, n):
        value = [int(x) for x in list(str(n))]
        value_next = sum([x * x for x in value])
        return value_next

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_set = set()
        while True:
            if n == 1:
                return True
            if n in num_set:
                return False
            num_next = Solution().transformNum(n)
            num_set.add(n)
            n = num_next

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while 5 ** i <= n:
            count += n // 5 ** i
            i += 1
        return count

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = 0
        for i in range(len(s)):
            result += temp.index(s[-1 - i]) * 26 ** i
        return result

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        if n > 0:
            return x * self.pow(x, n - 1)
        elif n < 0:
            return 1 / self.pow(x, -n)
        else:
            return 1

    def pow(self, x, n):
        if n == 1:
            return x
        if n == 2:
            return x * x
        result = self.pow(x, n // 2)
        if n % 2 == 0:
            return result * result
        else:
            return x * result * result

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left, right = 0, x
        while right - left > 1:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid
            else:
                left = mid
        return left

    def dividePositive(self, dividend, divisor):
        if dividend == 0 or dividend < divisor:
            return 0

        sum_now = 0
        word_next = 0
        count_now = 0

        while sum_now <= dividend:
            count_now += 1
            word_next += divisor
            sum_now += word_next

        divide_remained = self.dividePositive(dividend - sum_now + word_next, divisor)
        return sum(range(count_now)) + divide_remained

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend * divisor >= 0:
            result = self.dividePositive(abs(dividend), abs(divisor))
        else:
            result = -1 * self.dividePositive(abs(dividend), abs(divisor))
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return result

    def fractionNormalToDecimal(self, numerator, denominator):
        remainder = numerator % denominator
        index = 0
        remainder_dict = {remainder: index}
        divided_list = []
        while numerator < denominator:
            numerator *= 10
            index += 1
            divided = numerator // denominator
            divided_list.append(str(divided))
            remainder = numerator % denominator
            if remainder == 0:
                return "".join(divided_list)
            elif remainder in remainder_dict:
                remainder_ix = remainder_dict[remainder]
                divided_list.insert(remainder_ix, "(")
                divided_list.append(")")
                return "".join(divided_list)
            else:
                remainder_dict[remainder] = index

            numerator = remainder

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 将分子值提升到比分母大的值
        negative = 0
        if numerator * denominator < 0:
            negative = 1
        numerator = abs(numerator)
        denominator = abs(denominator)

        value = 0
        if numerator >= denominator:
            value = numerator // denominator
            numerator = numerator % denominator

        if numerator == 0:
            if negative:
                return "-" + str(value)
            else:
                return str(value)

        next_result = self.fractionNormalToDecimal(numerator, denominator)
        if negative == 1:
            return "-" + str(value) + "." + next_result
        else:
            return str(value) + "." + next_result


print(Solution().fractionToDecimal(-2147483648, 1))
