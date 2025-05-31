from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx, neg_idx, result = 0, 1, []
        for i in nums:
            if i > 0:
                result.insert(pos_idx, i)
                pos_idx += 2
            else:
                result.insert(neg_idx, i)
                neg_idx += 2
        return result


sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))