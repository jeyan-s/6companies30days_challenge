from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x not in "+-*/":
                stack.append(int(x))
            else:
                #print(stack)
                if x == '+':
                    x, y = stack.pop(), stack.pop()
                    z = x + y
                    stack.append(z)
                if x == '*':
                    x, y = stack.pop(), stack.pop()
                    z = x * y
                    stack.append(z)
                if x == '/':
                    x, y = stack.pop(), stack.pop()
                    z = y / x
                    if z < 0:
                        z = ceil(z)
                    
                    #print(x, y, z)
                    stack.append(floor(z))
                if x == '-':
                    x, y = stack.pop(), stack.pop()
                    z = y - x
                    stack.append(z)
        return floor(stack.pop())