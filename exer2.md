class Solution:
    def twoSum (self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complemet = target - num
            if complemet in num_map:
                return [num_map[complemet], i]
            num_map[num] = i
        return []
    
if __name__ == "__main__":
 sol = Solution()
 nums = [2, 7, 11, 15]
 target = 9
 print(sol.twoSum(nums, target))
