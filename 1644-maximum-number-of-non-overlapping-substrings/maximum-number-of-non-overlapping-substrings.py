class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        intervals = {}
        for i , c in enumerate(s):
            if not c in intervals: intervals[c] = [i , i]
            else: intervals[c][1] = i

        for c in intervals:
            l, r = intervals[c]
            while True:
                lcopy, rcopy = l, r
                for i in range(lcopy, rcopy + 1):
                    l = min(l, intervals[s[i]][0])
                    r = max(r, intervals[s[i]][1])
                if (lcopy, rcopy) == (l, r): break
                intervals[c] = (l, r)

        candidates = sorted(intervals.values(), key = lambda x: x[1])
        res = []
        prev = -1
        for start, end in candidates:
            if start > prev:
                res.append(s[start: end + 1])
                prev = end

        return res