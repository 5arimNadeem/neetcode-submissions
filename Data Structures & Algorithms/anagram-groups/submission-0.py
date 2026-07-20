class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # exact same characters 
        # a routine which will identify the exact same characters in both strings
        # looping through the string array 
        # hashmap, sorting
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        