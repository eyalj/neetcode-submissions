class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = {}
        for num in nums:
            if num not in length:
                left_length = length.get(num-1,0)
                right_length = length.get(num+1,0)
                current_length = left_length + right_length + 1
                length[num] = current_length
                length[num - left_length] = current_length
                length[num + right_length] = current_length
        return max(length.values(),default=0)
