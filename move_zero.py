from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
        return nums

sol = Solution()
print(sol.moveZeroes([0,0,1]))