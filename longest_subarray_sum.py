class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        right = 0
        count = 0
        while right < len(s):
            if s[right] not in substring:
                substring.add(s[right])
                right += 1
            else:
                if len(substring) > count:
                    count = len(substring)
                substring.remove(s[left])
                left += 1
            if len(substring) > count:
                count = len(substring)
        return count

sol = Solution()
print(sol.lengthOfLongestSubstring("dvdf"))