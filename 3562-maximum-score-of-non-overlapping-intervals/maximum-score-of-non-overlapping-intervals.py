class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervalsi = {}
        for i, (l, r, w) in enumerate(intervals):
            if not (l, r, w) in intervalsi: intervalsi[(l, r, w)] = i
        intervals = sorted(intervalsi)
        n = len(intervals)
        @cache
        def dp(i, rem):
            if rem == 0 or i == n: return 0, []
            skipw, skip_indices = dp(i + 1, rem)
            l, r, w = intervals[i]
            nexti = bisect.bisect_left(intervals, (r + 1,))
            nextw, next_indices = dp(nexti, rem - 1)
            takew = w + nextw
            take_indices = next_indices + [intervalsi[intervals[i]]]
            take_indices.sort()
            if takew > skipw: return (takew, take_indices)
            elif takew < skipw: return (skipw, skip_indices)
            if take_indices < skip_indices: return (takew, take_indices)
            else : return (skipw, skip_indices)
        return dp(0, 4)[1]
        