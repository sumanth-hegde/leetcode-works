from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:k]:
                nums[k] = nums[i]
                k += 1
        return k

sol = Solution()
print(sol.removeDuplicates([1,1,2]))