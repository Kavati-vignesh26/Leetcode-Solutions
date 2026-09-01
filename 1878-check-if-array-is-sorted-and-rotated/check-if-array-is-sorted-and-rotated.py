class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 : return True
        smaller = nums[0] < nums[-1]
        for i in range(1,n):
            if nums[i] < nums[i - 1]:
                if smaller: return False
                smaller = True
        return True
        