class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums: 
            d[num] += 1
        # heap = []
        for key, value in d.items():
            # print(key, "---", value)
            if value > 1:
                return True
        return False