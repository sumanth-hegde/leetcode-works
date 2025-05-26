from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
        count = 0
        one_count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                one_count = count
                count = 0
            else:
                count += 1
        if count == 0:
            count = one_count
        return count


sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))