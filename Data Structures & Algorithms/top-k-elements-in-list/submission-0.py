class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i,n in enumerate(nums):
            freq[n] = freq.get(n,0)+1
        
        heap = []
        for key,v in freq.items():
            heapq.heappush(heap,(v,key))
            while len(heap)>k:
                heapq.heappop(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        out = []
        while heap:
            v,key = heapq.heappop(heap)
            out.append(key)
        return out

        