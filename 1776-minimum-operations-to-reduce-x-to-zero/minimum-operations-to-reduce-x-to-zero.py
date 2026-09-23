class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        maxl = -1
        curr = 0
        l = 0
        for r in range(n):
            curr += nums[r]
            while l <= r and curr > target:
                curr -= nums[l]
                l += 1
            if curr == target:
                maxl = max(maxl, r - l + 1)
        return n - maxl if maxl != -1 else -1
        