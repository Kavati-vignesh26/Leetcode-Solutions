class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pmx = [nums[0]] * n
        smn = [nums[-1]] * n
        for i in range(1, n): pmx[i] = max(pmx[i - 1], nums[i])
        for i in range(n - 2, -1, -1): smn[i] = min(smn[i + 1], nums[i])
        for i in range(n):
            if pmx[i] - smn[i] <= k: return i
        return -1