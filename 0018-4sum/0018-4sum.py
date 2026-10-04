class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        output_set = set()
        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in seen:
                        quadruplet = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        output_set.add(quadruplet)
                    seen.add(nums[k])
        return [list(q) for q in output_set]