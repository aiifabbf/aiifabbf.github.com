from typing import *

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda v: v[0])
        roomFinishingTimes = []
        heapq.heapify(roomFinishingTimes)

        for v in intervals:
            if roomFinishingTimes:
                if heapq.nsmallest(1, roomFinishingTimes)[0] <= v[0]:
                    heapq.heappop(roomFinishingTimes)
                    heapq.heappush(roomFinishingTimes, v[1])
                else:
                    heapq.heappush(roomFinishingTimes, v[1])
            else:
                heapq.heappush(roomFinishingTimes, v[1])

        return len(roomFinishingTimes)

s = Solution()
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]])) # 2
print(s.minMeetingRooms([[7,10],[2,4]])) # 1
print(s.minMeetingRooms([[2,15],[36,45],[9,29],[16,23],[4,9]])) # 2