class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # charset takes 26 chars max 
        # we iterate over the entire string at max 26 times
        # time - O(n) and space O(n)
        charset = set(s)
        maxlen = 1
        for c in charset:
            # print(c)
            l = 0
            freq = {x:0 for x in charset}
            count = 0
            for r in range(0, len(s)):
                # print(l, r, s[l], s[r], count)
                freq[s[r]]+=1
                if s[r] != c:
                    count+=1
                while l<r and r-l+1 > k and k-count<0:
                    freq[s[l]]-=1
                    if s[l]!=c: count-=1
                    l+=1
                maxlen = max(maxlen, r-l+1)
        return maxlen
                



