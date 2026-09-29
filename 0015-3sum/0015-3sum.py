class Solution(object):

  def threeSum(self, nums):
    """:type nums: List[int]

    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
      # Skip duplicate elements for the first number
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left, right = i + 1, n - 1
      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if current_sum < 0:
          left += 1
        elif current_sum > 0:
          right -= 1
        else:
          res.append([nums[i], nums[left], nums[right]])

          # Skip duplicates for the second number
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          # Skip duplicates for the third number
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1

    return res