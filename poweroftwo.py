class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        if n == 1:
            return True
        sum_bits = 0
        while n:
            sum_bits += n % 2
            n = n/2
        if sum_bits == 1:
            return True
        return False
        