class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_indices = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in list_indices:
                return [list_indices[val], i]
            list_indices[nums[i]] = i
