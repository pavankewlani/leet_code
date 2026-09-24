class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            val = nums[i]
            digit_sum = 0
            while val > 0:
                digit_sum += val % 10
                val //= 10
            if digit_sum == i:
                return i
        return -1
        

        