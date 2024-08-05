# Time Complexity : O(n), where n is the number of tokens in the list
# Space Complexity : O(n), stack space
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # Ensure the result is truncated towards zero
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack.pop()

# Examples

# Example 1
tokens = ["2", "1", "+", "3", "*"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 9

# Example 2
tokens = ["4", "13", "5", "/", "+"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 6

# Example 3
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 22