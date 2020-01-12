class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}

        for string in strs:
            anagram = "".join(sorted(string))
            if anagram in mapping:
                mapping[anagram].append(string)
            else:
                mapping[anagram] = [string]

        return list(mapping.values())