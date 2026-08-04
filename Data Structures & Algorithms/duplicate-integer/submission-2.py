class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = {}
        for item in nums:
            if item in items:
                return True
            else:
                items.update({item: 1})
        return False