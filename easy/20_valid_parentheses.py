class Solution(object):
    def isValid(self, s):
        dic = {"(": ")", "[": "]", "{": "}",
               ")": "(", "]": "[", "}": "{"}
        open_b = ["(", "[", "{"]

        if len(s) % 2 != 0:
            return False
        lst = ""
        stack = []
        for i in s:
            if i in open_b:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif (dic[stack[-1]] != i and dic[i] != dic[stack[-1]]):
                return False
            else:
                lst += stack.pop() + i

        if len(lst) != 0:
            j = 0
            while j < len(lst):
                if dic[lst[j]] != lst[j + 1]:
                    return False
                j += 2
            return len(stack) == 0

        else:
            j = 0
            while j < len(stack):
                if dic[stack[j]] != [j + 1]:
                    return False
                j += 2
            return True
