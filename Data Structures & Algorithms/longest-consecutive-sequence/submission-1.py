class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        heuristics : 
        1. looping through array 
        2. sorting it 
        3. taking in view the sequecne record 
            
        """

        numSet = set(nums)

        longest = 0
        

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
