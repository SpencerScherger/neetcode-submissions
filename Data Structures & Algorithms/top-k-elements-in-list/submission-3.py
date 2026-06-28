class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            freq_buckets[value].append(key)
        
        res = []
        for b in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[b]:
                res.append(num)
                if(len(res) == k):
                    return res