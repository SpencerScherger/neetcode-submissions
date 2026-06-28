class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Construct frequency hashmap
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for key in freq.keys():
            heapq.heappush(heap, (freq[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
