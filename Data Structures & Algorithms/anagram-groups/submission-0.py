class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            tmp = [0 for _ in range(26)]
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            
            key = tuple(tmp)
            d[key].append(s)
        
        return list(d.values())
        
        