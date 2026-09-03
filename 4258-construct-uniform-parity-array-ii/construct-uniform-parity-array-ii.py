class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return all(n % 2 == 0 for n in nums1) or all(n % 2 == 1 for n in nums1) or min(nums1) % 2 == 1