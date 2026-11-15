class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        even = 1
        odd = 0
        ans = 0

        for num in arr:
            if num % 2 == 0:
                even += 1
            else:
                even, odd = odd + 1, even

            ans = (ans + odd) % mod

        return ans