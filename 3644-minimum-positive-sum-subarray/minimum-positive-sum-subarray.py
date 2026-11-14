class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = inf
        for i in range(n):
            curr = 0
            count = 0
            for j in range(i, n):
                count += 1
                curr += nums[j]
                if count < l : continue
                if count > r : break
                if curr > 0 : res = min(res, curr)
        return res if res != inf else -1
        