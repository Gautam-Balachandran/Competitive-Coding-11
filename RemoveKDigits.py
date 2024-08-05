# Time Complexity : O(n), where n is the length of the string num
# Space Complexity : O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # base case
        if not num or len(num) == k:
            return "0"
        
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        # Convert the stack back to a string and remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"

# Examples
num = "1432219"
k = 3
solution = Solution()
print(solution.removeKdigits(num, k))  # Output: "1219"
num = "10200"
k = 1
solution = Solution()
print(solution.removeKdigits(num, k))  # Output: "200"
num = "10"
k = 2
solution = Solution()
print(solution.removeKdigits(num, k))  # Output: "0"