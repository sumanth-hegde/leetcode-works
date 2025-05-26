class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi, curr_sum, left = -1, 0, 0
        while left <= k:
            curr_sum += nums[left]
            left += 1
            if curr_sum > maxi:
                maxi = curr_sum
                curr_sum = 0
            if left == k:
                k += 1
        return maxi

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))