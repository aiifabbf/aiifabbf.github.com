class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []

        for log in logs:
            if log.split()[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        
        return sorted(letterLogs, key=lambda v: " ".join(v.split()[1: ] + v.split()[0: 1])) + digitLogs