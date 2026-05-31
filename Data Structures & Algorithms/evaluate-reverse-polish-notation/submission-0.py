class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in ('+', '-', '*', '/'):
                stack.append(int(c))  #  cast to int here
            else:
                b = stack.pop()  # second operand
                a = stack.pop()  # first operand
                
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
                elif c == '*':
                    stack.append(a * b)
                elif c == '/':
                    stack.append(int(a / b))  # truncates toward zero
            
        return stack[0]