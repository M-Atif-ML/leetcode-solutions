class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        slow = 0
        max_len = 0

        for fast in range(len(s)):
            while s[fast] in sset:
                sset.remove(s[slow])
                slow += 1
            sset.add(s[fast])
            max_len = max(max_len,fast-slow+1) # because index starts with zero

        return max_len
