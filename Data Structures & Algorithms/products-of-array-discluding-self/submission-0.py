class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n
        left_products = [0] * n
        right_products = [0] * n

        left_products[0] = right_products[n - 1] = 1

        for i in range(1, n):
            left_products[i] = nums[i - 1] * left_products[i - 1]
        for i in range(n - 2, -1, -1):
            right_products[i] = nums[i + 1] * right_products[i + 1]
        for i in range(n):
            res[i] = left_products[i] * right_products[i]
        return res