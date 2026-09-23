from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            print("outer")
            print(stack)
            # while current temp is greater than the temp at index on top of stack
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                print("after removing greater successive element")
                print("removed",prev_index)
                print(stack)
                res[prev_index] = i - prev_index
                print(res[prev_index])
            stack.append(i)

        return res
