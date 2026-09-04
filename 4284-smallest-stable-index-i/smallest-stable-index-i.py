class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            mn, mx = inf, -inf
            for j in range(i+1): mx = max(mx, nums[j])
            for j in range(i,n): mn = min(mn, nums[j])
            if mx - mn <= k : return i
        return -1