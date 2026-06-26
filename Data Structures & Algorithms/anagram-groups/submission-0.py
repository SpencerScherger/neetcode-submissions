class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        base = ord("a")
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - base] += 1

            arr = tuple(arr)
            if res.get(arr) is None:
                res[arr] = []
            res.get(arr).append(s)
        
        return(list(res.values()))
            


            