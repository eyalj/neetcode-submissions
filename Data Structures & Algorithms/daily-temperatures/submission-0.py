from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                update_item = stack.pop()
                result[update_item[1]] = i - update_item[1]
            stack.append((temp,i))
        return result
                    