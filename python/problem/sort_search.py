# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution(object):
    def goodBadVersion(self, good, bad, n):
        if n <= good:
            return None
        isBad = isBadVersion(n)
        if isBad:
            bad = n
        else:
            good = n

        if bad - good == 1:
            return bad
        median = (good + bad) // 2
        return self.goodBadVersion(good, bad, median)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.goodBadVersion(0, n, 2//2)

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        ix = 0
        for i in range(n):

            while nums2[i] > nums1[ix] and ix < m+i:
                ix += 1
            nums1.insert(ix, nums2[i])
            nums1.pop()

