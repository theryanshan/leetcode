# Time: O(nlogn)
# Space: O(1)
# Tip: sort the intervals by start time, then check if the start time of next interval is smaller than the end time of previous interval


class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


s = Solution()
ans = s.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
print(ans)
