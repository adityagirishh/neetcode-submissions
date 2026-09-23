
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        res = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))  # sort letters to create a signature key
            res[key].append(word)
        return list(res.values())

