class Solution(object):
    def isValid(self, s):
        stack = []
        Map = {")" : "(", "]" :"[", "}" : "{"}

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            
            if not stack or stack[len(stack) - 1] != Map[c]:
                return False
            stack.pop()
        return not stack