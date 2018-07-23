class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        composite_dict = {}
        prime_dict = {}
        primes_count = 0
        for i in range(2, n):
            if i not in composite_dict:
                primes_count += 1
                prime_dict[primes_count] = i
                composite_dict[i] = 1
            j = 1
            while j <= primes_count and i * prime_dict[j] < n:
                composite_dict[i * prime_dict[j]] = 1
                if i % prime_dict[j] == 0:
                    break
                j += 1
        return primes_count

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n > 3:
            if n % 3 != 0:
                return False
            n /= 3
        if n == 3:
            return True
        else:
            return False

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                result.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                result.append("Fizz")
            elif (i + 1) % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i + 1))
        return result

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        str_list = list(s)
        len_list = len(str_list)
        result = 0
        if len_list ==0:
            return None
        elif len_list == 1:
            return value_dict[str_list[0]]
        for i in range(1, len_list):
            value_second = value_dict[str_list[i]]
            value_fist = value_dict[str_list[i-1]]
            if value_fist >= value_second:
                result += value_fist
            else:
                result -= value_fist
        result += value_dict[str_list[-1]]
        return result
