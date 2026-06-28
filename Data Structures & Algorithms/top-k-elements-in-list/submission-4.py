class Solution:
    # TC: O(n)
    # SC: O(n)

    '''
    Bucket sort solution:
    1. Build freq map
    2. Create freq_buckets where freq_buckets[i] stores a list of the numbers appearing i times
    3. Loop backwards and append to result list
    4. End loop early once result list length == k
    '''
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