class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            char = [0]*26
            for c in s:
                char[ord(c)-ord('a')]+=1
            if tuple(char) in groups:
                groups[tuple(char)].append(s)
            else:
                 groups[tuple(char)] = [s]
        return list(groups.values())