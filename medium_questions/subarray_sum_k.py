from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum, count = 0, 0
        mapp = {0:1}
        for num in nums:
            pre_sum += num
            count += mapp.get(pre_sum - k, 0)
            mapp[pre_sum] = mapp.get(pre_sum, 0) + 1
        return count


sol = Solution()
print(sol.subarraySum([1,1,1], 2))