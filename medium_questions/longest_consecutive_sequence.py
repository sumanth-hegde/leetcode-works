""" Brute force solution """

def longest_consecutive(nums):
    if len(nums) <= 1:
        return nums
    count, n, sorted_nums = 0, len(nums), sorted(nums)
    for i in range(1, n):
        if i == sorted_nums[i-1]:
            count += 1
    return count


print(longest_consecutive([100,4,200,1,3,2]))

""" Optimal Solution, TC: O(n), SC: O(n) """

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, num_set = 0, set(nums)
        for i in num_set:
            if (i - 1) not in num_set:
                length = 1
                while (i + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest