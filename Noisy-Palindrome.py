class Solution:
    def solve(self, s):
        res = []
        for i in range(len(s)):
            if s[i].islower():
                res.append(s[i])
        return res[::-1] == res