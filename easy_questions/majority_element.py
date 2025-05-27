from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, ele = 0, 0
        for num in nums:
            if count == 0:
                ele = num
            if num == ele:
                count += 1
            else:
                count -= 1
        return ele


sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))