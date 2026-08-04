class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(0,len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]],i]
            diff.update({target-nums[i]:i})
        return [0,0]