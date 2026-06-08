class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}

        for char in s:
            h1[char] = h1.get(char,0)+1
        
        for char in t:
             h2[char] = h2.get(char,0)+1
        
        
        if len(h1)!=len(h2): return False

        for k,v in h1.items():
            if k not in h2 or h2[k]!=v:
                return False
        
        return True
