from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = deque()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while min_stack and temperatures[i] >= min_stack[-1][0]:
                min_stack.pop()
            if min_stack:
                result[i] = min_stack[-1][1] - i 
            min_stack.append((temperatures[i],i))
        return result
                    