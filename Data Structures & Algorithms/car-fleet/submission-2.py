from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info_combine = list(zip(position,speed))
        info_combine.sort(reverse=True)
        stack = deque()
        for i in range(0, len(info_combine)):
            p, s = info_combine[i]
            arrival_time = (target - p)/s
            if not stack:
                stack.append(arrival_time)
            elif arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)
