class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = {j:i for i,j in zip('([{', ')]}')}
        stack = []
        for p in s:
            if p in right:
                if stack and stack[-1] == right[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return not stack

s = Solution()
print(s.isValid(input()))
