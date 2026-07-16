class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '' : return 0
        maxlen = 0
        freq = defaultdict(int)
        l = 0
        for r in range(len(s)):
            freq[s[r]]+=1
            while l<=r and freq[s[r]]>1:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
                
            maxlen = max(maxlen, r-l+1)
        return maxlen

            



