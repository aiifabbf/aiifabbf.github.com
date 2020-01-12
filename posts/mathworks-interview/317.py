from typing import *

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])
        buildings = set()
        obstacles = set()

        for rowIndex, row in enumerate(grid):

            for columnIndex, box in enumerate(row):
                position = (rowIndex, columnIndex)
                if box == 1:
                    buildings.add(position)
                elif box == 2:
                    obstacles.add(position)

        positionDistanceMapping = dict()
        queue = []
        traveled = set()

        for building in buildings:
            # queue = [building]
            queue.clear()
            queue.append(building)
            traveled.clear()
            distance = 0

            while queue:
                size = len(queue)

                for _ in range(size):
                    node = queue.pop(0)
                    rowIndex, columnIndex = node
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1)
                    ]

                    for neighbor in neighbors:
                        if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in traveled:
                            queue.append(neighbor)

                    traveled.add(node)
                    if node not in buildings and node not in obstacles:
                        if node not in positionDistanceMapping:
                            positionDistanceMapping[node] = dict()
                            positionDistanceMapping[node][building] = distance
                        else:
                            positionDistanceMapping[node][building] = distance

                distance += 1

        res = float("+inf")

        for position, distanceToBuildings in positionDistanceMapping.items():
            if len(distanceToBuildings) != len(buildings):
                continue
            else:
                res = min(res, sum(distanceToBuildings.values()))

        if res == float("+inf"):
            return -1
        else:
            return res

s = Solution()
print(s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])) # 7
print(s.shortestDistance([[2,0,0,2,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,1,2,0,2,0,1,1,0],[0,1,0,1,1,2,0,0,2,0,0,2,0,2,2,0,2,0,2,0,0,0,0,0,0,0,0,0],[1,0,0,1,2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,2],[0,0,2,2,2,1,0,0,2,0,0,0,0,0,0,0,0,0,2,2,2,2,1,0,0,0,0,0],[0,2,0,2,2,2,2,1,0,0,0,0,1,0,2,0,0,0,0,2,2,0,0,0,0,2,2,1],[0,0,2,1,2,0,2,0,0,0,2,2,0,2,0,2,2,2,2,2,0,0,0,0,2,0,2,0],[0,0,0,2,1,2,0,0,2,2,2,1,0,0,0,2,0,2,0,0,0,0,2,2,0,0,1,1],[0,0,0,2,2,0,0,2,2,0,0,0,2,0,2,2,0,0,0,2,2,0,0,0,0,2,0,0],[2,0,2,0,0,0,2,0,2,2,0,2,0,0,2,0,0,2,1,0,0,0,2,2,0,0,0,0],[0,0,0,0,0,2,0,2,2,2,0,0,0,0,0,0,2,1,0,2,0,0,2,2,0,0,2,2]])) # 