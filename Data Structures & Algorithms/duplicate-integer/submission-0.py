class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # # 
        # count varibale 
        # 1. loop through the array 
        # 2. if appear for the first time 
        #     count += 1
        # 3. for keeping the check of it hashset will be used 
        #     we will keep adding the values in it 
        #     and keep incrementing 
        # 4. return True
        # 5. return False
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False