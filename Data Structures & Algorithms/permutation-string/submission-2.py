class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        s1map = defaultdict(int)
        for c in s1:
            s1map[c]+=1
        s2map = defaultdict(int)
        i = 0
        while i <len(s2):
            c = s2[i]
            l = i
            while i<len(s2) and s2[i] in s1map and s1map[s2[i]]>s2map[s2[i]]:
                s2map[s2[i]]+=1
                i+=1

            if s1map==s2map: return True
            else: 
                s2map = defaultdict(int)
                i = l+1

        return False


            
