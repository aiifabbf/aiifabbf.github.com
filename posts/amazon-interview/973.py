class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda v: v[0] ** 2 + v[1] ** 2)[: K]