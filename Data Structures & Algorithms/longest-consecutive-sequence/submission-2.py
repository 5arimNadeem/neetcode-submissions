class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # print(nums)

        hash_set = set(nums)
        longest = 0
        for num in nums:
            # hash_set.add(num)
            if (num - 1) not in hash_set:
                length = 0
                while (num + length) in hash_set:
                    length += 1
                longest = max(length, longest)
        # print(hash_set)
        return longest