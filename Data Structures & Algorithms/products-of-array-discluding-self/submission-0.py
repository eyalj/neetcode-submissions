class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result  = []
        sum = 1
        for num , i in zip(nums,range(0,len(nums))):
            result.append(sum)
            sum *= num
        sum = 1
        for num , i in zip(reversed(nums),range(len(nums)-1,-1,-1)):
            result[i] *= sum
            sum *= num
        return result