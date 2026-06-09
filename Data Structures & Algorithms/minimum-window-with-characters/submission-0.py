class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = {}
        for c in t:
            tfreq[c] = tfreq.get(c, 0) + 1
        
        sfreq = {}
        have, need = 0, len(tfreq)
        l = 0
        res = ""
        minwin = float("inf")

        for r, c in enumerate(s):
            sfreq[c] = sfreq.get(c, 0) + 1
            if c in tfreq and sfreq[c] == tfreq[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < minwin:
                    minwin = r - l + 1
                    res = s[l:r+1]
                sfreq[s[l]] -= 1
                if s[l] in tfreq and sfreq[s[l]] < tfreq[s[l]]:
                    have -= 1
                l += 1
        
        return res