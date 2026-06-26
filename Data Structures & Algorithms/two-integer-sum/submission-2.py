class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i
            
        for i, n in enumerate(nums):
            diff = target - n
            if indices.get(diff) is not None and i != indices.get(diff):
                if i < indices[target - n]:
                    return [i, indices[target - n]]
                return [indices[target - n], i]
            