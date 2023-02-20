class Solution:
    def longestPrefix(self, s: str) -> str:
        n = [0] + [None] * (len(s) - 1)
        for i in range(1, len(s)):
            k = n[i - 1] # trying length k + 1
            while (k > 0) and (s[i] != s[k]):
                k = n[k - 1]
            if s[i] == s[k]:
                k += 1
            n[i] = k
        return s[:n[-1]]
