from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))

            elif token == "+":
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(o2 + o1)

            elif token == "-":
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(o2 - o1)

            elif token == "*":
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(o2 * o1)

            elif token == "/":
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(int(o2 / o1))

        return stack.pop()