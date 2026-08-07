class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_counts = {}

        for i in range(len(s)):

            char_s = s[i]
            if char_s in char_counts:
                char_counts[char_s] += 1
            else:
                char_counts[char_s] = 1
            
            char_t = t[i]
            if char_t in char_counts:
                char_counts[char_t] -= 1
            else:
                char_counts[char_t] = -1
            
        for key in char_counts:
            if char_counts[key] != 0:
                return False
        return True