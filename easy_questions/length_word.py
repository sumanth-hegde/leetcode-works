class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        t = ""
        while i >= 0 and s[i] != ' ':
            t += s[i]
            length += 1
            i -= 1
        return length

sol = Solution()
print(sol.lengthOfLastWord("luffy is still joyboy      "))