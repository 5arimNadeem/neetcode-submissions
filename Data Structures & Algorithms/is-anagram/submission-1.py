class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = []
        for char in s:
            slist.append(char)
        for char in t:
            if char in slist:
                slist.remove(char)
            else:
                return False
        return not bool(len(slist))