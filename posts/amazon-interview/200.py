class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        rowCount = len(grid)
        columnCount = len(grid[0])
        mapping = {}

        for rowIndex, row in enumerate(grid):

            for columnIndex, box in enumerate(row):
                if box == "1":
                    position = (rowIndex, columnIndex)
                    mapping[position] = mapping.get(position, position)
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1),
                    ]

                    for neighbor in neighbors:
                        if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount and grid[neighbor[0]][neighbor[1]] == "1":
                            mapping[neighbor] = mapping.get(neighbor, neighbor)
                            self.union(mapping, position, neighbor)

        return len({self.rootOf(mapping, k) for k in mapping.keys()})
        
    def union(self, mapping: dict, p: "Type", q: "Type") -> None:
        rootOfP = self.rootOf(mapping, p)
        rootOfQ = self.rootOf(mapping, q)
        mapping[rootOfP] = rootOfQ

    def rootOf(self, mapping: dict, p: "Type") -> "Type":

        while p != mapping[p]:
            mapping[p] = mapping[mapping[p]]
            p = mapping[p]

        return p

    def isConnected(self, mapping: dict, p: "Type", q: "Type") -> bool:
        return self.rootOf(mapping, p) == self.rootOf(mapping, q)