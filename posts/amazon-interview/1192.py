class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
    def rootOf(self, mapping: dict, p: "Type") -> "Type":

        while p != mapping[p]:
            mapping[p] = mapping[mapping[p]]
            p = mapping[p]

        return p
    
    def union(self, mapping: dict, p: "Type", q: "Type") -> None:
        rootOfP = self.rootOf(mapping, p)
        rootOfQ = self.rootOf(mapping, q)
        mapping[rootOfP] = rootOfQ

    def isConnected(self, mapping: dict, p: "Type") -> bool:
        return self.rootOf(mapping, p) == self.rootOf(mapping, q)