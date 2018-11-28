class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        valid = True
        for symbol in s:
            if len(l) == 0:
                l.append(symbol)
                continue;
            word = l[len(l)-1]
            if symbol == ')':
                if word == '(': l.pop()
                else: return False
            elif symbol == ']':
                if word == '[': l.pop()
                else: return False
            elif symbol == '}':
                if word == '{': l.pop()
                else: return False
            else: l.append(symbol)

        if len(l) != 0: valid = False
        return valid

s = Solution()
print(s.isValid(input()))
