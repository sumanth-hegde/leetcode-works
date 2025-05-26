class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_freq, left, curr_sum = 1, 0, 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            window_size = right - left + 1

            while window_size * nums[right] - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
                window_size -= 1
            max_freq = max(max_freq, window_size)

        return max_freq

sol = Solution()
print(sol.maxFrequency([1,4,8,13], 5))