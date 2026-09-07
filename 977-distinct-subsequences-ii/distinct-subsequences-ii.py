class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)
        last = {}
        for i in range(n):
            dp[i + 1] = dp[i] * 2
            if s[i] in last : dp[i + 1] -= dp[last[s[i]]]
            last[s[i]] = i 
        return (dp[-1] -1) % (10 ** 9 + 7)

        