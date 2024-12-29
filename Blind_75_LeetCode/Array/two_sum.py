class Solution:
    def twosum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
result = Solution()
nums = [2,7,11,15]
target = 9
result1 = result.twosum(nums, target)
print(result1)
