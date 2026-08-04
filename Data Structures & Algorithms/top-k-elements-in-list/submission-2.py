class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        duplicate_k = {}
        for num in nums:
            if(num not in duplicate_k):
                duplicate_k[num] = 1
            else:
                 duplicate_k[num] +=1
        numbers_of_duplicates = [[] for _ in range(len(nums) + 1)]


        for number in duplicate_k:
            numbers_of_duplicates[duplicate_k[number]].append(number)

        result = []
        for duplicate_k in reversed(numbers_of_duplicates):
            if k == 0:
                return result   
            for number in duplicate_k:
                if k == 0: 
                    return result
                result.append(number)
                k-=1     
        return result