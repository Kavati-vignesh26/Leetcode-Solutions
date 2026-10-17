class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        initial = {n : i for i, n in enumerate(nums)}
        def helper(x):
            total = 0
            while x :
                total += x % 10
                x //= 10
            return total
        nums.sort()
        nums.sort(key = lambda x : helper(x))
        visited = set()
        res = 0
        for i in range(len(nums)):
            if i in visited: continue
            j = i
            steps = 0
            while not j in visited:
                visited.add(j)
                steps += 1
                j = initial[nums[j]]
            res += steps - 1
        return res
        