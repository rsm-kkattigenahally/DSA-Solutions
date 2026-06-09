class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='': return 0
        freq = {}
        l = 0
        maxl = 0
    
        for r in range(len(s)):
            freq[s[r]]= freq.get(s[r],0)+1
            while l<=r and freq[s[r]]>1:
                freq[s[l]]-=1
                if freq[s[l]]==0: del freq[s[l]]
                l+=1
            maxl = max(maxl, r-l+1)
        return maxl
            



